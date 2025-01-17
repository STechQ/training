from ultralytics import YOLO

model = YOLO('../runs/train/weights/best.pt')
model.predict("imagelanding.png", save=True, conf=0.5, iou=0)


# results = model('Frame 17959.png')  

# for index, result in enumerate(results):
#     boxes = result.boxes  # Boxes object for bounding box outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     keypoints = result.keypoints  # Keypoints object for pose outputs
#     probs = result.probs  # Probs object for classification outputs
#     obb = result.obb  # Oriented boxes object for OBB outputs
#     result.show()  # display to screen
#     result.save(filename="result.jpg")
#     # crop_filename = f"results/crop_{index}.jpg"
#     # result.save_crop(crop_filename)


# model = YOLO('yolo11n.pt')
# results = model('dogs.jpg')  

# for index, result in enumerate(results):
#     boxes = result.boxes  # Boxes object for bounding box outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     keypoints = result.keypoints  # Keypoints object for pose outputs
#     probs = result.probs  # Probs object for classification outputs
#     obb = result.obb  # Oriented boxes object for OBB outputs
#     result.show()  # display to screen
#     result.save(filename="result.jpg")
#     crop_filename = f"results/crop_{index}.jpg"
#     result.save_crop(crop_filename)