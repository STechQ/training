import os
import azure.functions as func
import logging
from ultralytics import YOLO
import requests
from PIL import Image
from io import BytesIO
import json
import time
import base64

MODEL_PATH = 'runs/train/weights/best.pt'
model = YOLO(MODEL_PATH)

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# CROPPED_IMAGES_DIR = "cropped_images"
# os.makedirs(CROPPED_IMAGES_DIR, exist_ok=True)

def resize_with_padding(image, target_size=(640, 640), fill_color=(114, 114, 114)):
    original_width, original_height = image.size
    target_width, target_height = target_size
    scale = min(target_width / original_width, target_height / original_height)
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)

    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    padded_image = Image.new("RGB", target_size, fill_color)

    upper_left_x = (target_width - new_width) // 2
    upper_left_y = (target_height - new_height) // 2
    padded_image.paste(resized_image, (upper_left_x, upper_left_y))

    return padded_image

def get_image_url_from_request(req):
    image_url = req.params.get('image_url')
    if not image_url:
        try:
            req_body = req.get_json()
            image_url = req_body.get('image_url')
        except ValueError:
            raise ValueError("Missing or invalid image_url in request.")
    return image_url

def download_image(image_url):
    response = requests.get(image_url)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    return resize_with_padding(img)

def encode_image_to_base64(image):
    """Encodes an image to base64 format."""
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    encoded_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return encoded_image

def detect_objects(image, model):
    results = model(image, conf=0.4, iou=0.5)
    detections = []

    # results[0].save_crop(CROPPED_IMAGES_DIR)

    for i, result in enumerate(results[0].boxes.data):
        box, conf, cls = result[:4], result[4], int(result[5])

        x1, y1, x2, y2 = map(int, box)

        cropped_image = image.crop((x1, y1, x2, y2))

        cropped_image_base64 = encode_image_to_base64(cropped_image)

        detections.append({
            'id': f'EdtrComp_{i+1}',
            'class': model.names[cls],
            'confidence': float(conf),
            'bbox': [float(x) for x in box],
            'cropped_image': cropped_image_base64
        })
    
    return detections

@app.route(route="func_createui_yolo11/predict")
def func_createui_yolo11(req: func.HttpRequest) -> func.HttpResponse:
    try:
        image_url = get_image_url_from_request(req)
        img = download_image(image_url)

        start_time = time.time()
        detections = detect_objects(img, model)
        processing_time = time.time() - start_time

        response = {
            'detections': detections,
            'metadata': {
                'processing_time_seconds': processing_time,
                'input_image_shape': img.size,
                'num_detections': len(detections)
            }
        }
        return func.HttpResponse(json.dumps(response), status_code=200, mimetype="application/json")
    except ValueError as ve:
        logging.error(f"Input error: {ve}")
        return func.HttpResponse(str(ve), status_code=400)
    except Exception as e:
        logging.error(f"Unexpected error: {e}", exc_info=True)
        return func.HttpResponse("Internal server error.", status_code=500)
