import os
from ultralytics import YOLO

def train():
    model = YOLO('yolo11m.pt')

    dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(dir, '../create-ui-datasetv3', 'data.yaml')

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found at: {data_path}")

    print("Starting training...")
    train_results = model.train(    
        data=data_path,
        epochs=300,
        imgsz=640,
        batch=16,
        project='runs/train',
        name='create-ui-training-exp3'
    )
    print("Training complete. Results: ", train_results)

if __name__ == '__main__':
    train()