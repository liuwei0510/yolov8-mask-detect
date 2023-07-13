from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('./runs/detect/train2/weights/best.pt')

# Define path to directory containing images and videos for inference
source = './test/test/images'
#source = 'me-test.jpg'
# Run inference on the source
results = model(source, stream=True)  # generator of Results objects

model.predict(source, save=True, imgsz=640, conf=0.5)

