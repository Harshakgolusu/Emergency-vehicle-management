from ultralytics import YOLO

# Load the pretrained YOLOv8s model
model = YOLO('yolov8s.pt') 

# Make predictions on the images in 'C:/Users/harsh/OneDrive/Desktop/aiot/train/images'
model.train('C:/Users/harsh/OneDrive/Desktop/aiot/train/images', save=True, imgsz=640, conf=0.3, show=True)
# results=model.train(data='data.yaml',epochs=5,imgsz=640,batch=10,workers=10,device=0)
