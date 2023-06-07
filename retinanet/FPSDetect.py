import numpy as np
import torch
import csv
import cv2
import time

# from visualize_single_image.py
def load_classes(csv_reader):
    result = {}

    for line, row in enumerate(csv_reader):
        line += 1

        try:
            class_name, class_id = row
        except ValueError:
            raise(ValueError('line {}: format should be \'class_name,class_id\''.format(line)))
        class_id = int(class_id)

        if class_name in result:
            raise ValueError('line {}: duplicate class name: \'{}\''.format(line, class_name))
        result[class_name] = class_id
    return result
    
model = None
labels = None

def init():
    class_list = './class_list.csv'
    model_path = './model_final.pt'
    global model
    global labels
    with open(class_list, 'r') as f:
        classes = load_classes(csv.reader(f, delimiter=','))

    labels = {}
    for key, value in classes.items():
        labels[value] = key

    model = torch.load(model_path)

    if torch.cuda.is_available():
        model.half()
        model = model.cuda()

    model.training = False
    model.eval()


def detect(img0):
    """
    :param img0: 要檢測的圖像
    :return: {'class': cls(目標類型), 'conf': conf(置信分數), 'position': xywh(目標螢幕座標)}
    """
    image = img0
    image_orig = img0.copy()

    rows, cols, cns = image.shape

    smallest_side = min(rows, cols)

    # rescale the image so the smallest side is min_side
    min_side = 608
    max_side = 1024
    scale = min_side / smallest_side

    # check if the largest side is now greater than max_side, which can happen
    # when images have a large aspect ratio
    largest_side = max(rows, cols)

    if largest_side * scale > max_side:
        scale = max_side / largest_side

    # resize the image with the computed scale
    image = cv2.resize(image, (int(round(cols * scale)), int(round((rows * scale)))))
    rows, cols, cns = image.shape

    pad_w = 32 - rows % 32
    pad_h = 32 - cols % 32

    new_image = np.zeros((rows + pad_w, cols + pad_h, cns)).astype(np.float32)
    new_image[:rows, :cols, :] = image.astype(np.float32)
    image = new_image.astype(np.float32)
    image /= 255
    image -= [0.485, 0.456, 0.406]
    image /= [0.229, 0.224, 0.225]
    image = np.expand_dims(image, 0)
    image = np.transpose(image, (0, 3, 1, 2))

    global model
    global labels

    detections = []
    with torch.no_grad():
        image = torch.from_numpy(image)
        if torch.cuda.is_available():
            image = image.cuda()
            image = image.half()

        print(image.shape, image_orig.shape, scale)
        predict_start = time.time()
        if torch.cuda.is_available():
            scores, classification, transformed_anchors = model(image)
        else:
            scores, classification, transformed_anchors = model(image.cuda().float())
        predict_time = time.time() - predict_start
        # for debug
        print("scores: ", scores) # save the stores of each box
        print("classification: ", classification) # save the labels of each box
        print("transofmed_anchors: ", transformed_anchors) # save the bbox of each box
        idxs = np.where(scores.cpu() > 0.5)

        for j in range(idxs[0].shape[0]):
            # for each box
            bbox = transformed_anchors[idxs[0][j], :]

            x1 = int(bbox[0] / scale)
            y1 = int(bbox[1] / scale)
            x2 = int(bbox[2] / scale)
            y2 = int(bbox[3] / scale)
            w  = x2-x1
            h  = y2-y1
            # assert x1 > x2 or y1 > y2 or w < 0 or h < 0
            xywh = [x1, y1, w, h]
            xywh = [round(x) for x in xywh]
            [xywh[0] - xywh[2] // 2, xywh[1] - xywh[3] // 2, xywh[2],
                    xywh[3]]
            cls = labels[int(classification[idxs[0][j]])]
            print(bbox, classification.shape)
            score = scores[j]
            # caption = '{} {:.3f}'.format(label_name, score)
            # draw_caption(img, (x1, y1, x2, y2), label_name)
            # draw_caption(image_orig, (x1, y1, x2, y2), caption)
            # cv2.rectangle(image_orig, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)
            detections.append({'class': cls, 'score': score, 'position': xywh})
    return detections, predict_time