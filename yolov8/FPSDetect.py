import numpy as np
import torch
from ultralytics import YOLO
from models.experimental import attempt_load
from utils.datasets import letterbox
from utils.general import check_img_size, non_max_suppression, scale_coords, xyxy2xywh
import warnings

warnings.filterwarnings("ignore")
# choose device
device = torch.device('cpu')  # 'cuda' if torch.cuda.is_available() else 'cpu')
half = device.type != 'cpu'
# Load model
model_name = r'best.pt'
model = YOLO(model_name)

def detect(img0):
    """
    :param img0: the image we want to detect
    :return: {'class': cls(classification), 'conf': conf(confidence), 'position': xywh(screen coordinate)}
    """
    detections = []
    conf = 0.25
    iou = 0.45
    results = model.predict(img0, device=device, conf=conf, iou=iou)
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

        print("test 1")
        for j in range(len(boxes)):
            xywh = xywhs[j].tolist()
            print("test 2")
            xywh = [round(x) for x in xywh]
            print("test 3")
            xywh = [xywh[0] - xywh[2] // 2, xywh[1] - xywh[3] // 2, xywh[2],
                    xywh[3]]  # detect target's position，format：（left，top，w，h）
            print("test 4")
            cls = names[int(clss[j])]
            print("test 5")
            conf = float(confs[j])
            print("test 6")
            detections.append({'class': cls, 'conf': conf, 'position': xywh})
            print("test 7")
        
    return detections