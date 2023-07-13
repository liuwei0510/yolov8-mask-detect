from ultralytics import YOLO

# Load a model
model = YOLO('yolov8s-pose.pt')  # load an official model
#model = YOLO('path/to/best.pt')  # load a custom model

# Predict with the model
results = model('hutao.jpg')  # predict on an image
source = 'hutao.jpg'
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Class probabilities for classification outputs
    print(keypoints)

model.predict(source, save=True, imgsz=640, conf=0.5)
