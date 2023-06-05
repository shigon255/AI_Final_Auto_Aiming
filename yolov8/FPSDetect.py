import numpy as np
import torch
from ultralytics import YOLO
from models.experimental import attempt_load
from utils.datasets import letterbox
from utils.general import check_img_size, non_max_suppression, scale_coords, xyxy2xywh
import warnings

warnings.filterwarnings("ignore")
# choose device
print(torch.cuda.is_available())
# Load model
model_name = r'best.pt'
model = YOLO(model_name)

def detect(img0):
    """
    :param img0: the image we want to detect
    :return: {'class': cls(classification), 'conf': conf(confidence), 'position': xywh(screen coordinate)}
    """
    if img0 is None:
        return []
    detections = []
    conf = 0.25
    iou = 0.45
    results = model.predict(img0, conf=conf, iou=iou,half = True)
    for i in range(len(results)):
        print("Box " + str(i))
        result = results[i]
        boxes = result.boxes
        xywhs = boxes.xywh
        clss = boxes.cls
        confs = boxes.conf
        masks = result.masks
        probs = result.probs
        names = result.names

        for j in range(len(boxes)):
            xywh = xywhs[j].tolist()
            xywh = [round(x) for x in xywh]            
            xywh = [xywh[0] - xywh[2] // 2, xywh[1] - xywh[3] // 2, xywh[2],
                    xywh[3]]  # detect target's position，format：（left，top，w，h）
            cls = names[int(clss[j])]
            conf = float(confs[j])
            detections.append({'class': cls, 'conf': conf, 'position': xywh})
        
    return detections