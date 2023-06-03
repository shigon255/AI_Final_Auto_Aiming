import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
print(torch.cuda.device_count())


from ultralytics import YOLO
model = YOLO("yolov8n.yaml")
# You can change the parameter
model.train(data = "apex.yaml",
            mode = "detect",
            epochs = 50,
            imgsz = 640,
            device = "0",
            batch = 16,
            workers = 0)
