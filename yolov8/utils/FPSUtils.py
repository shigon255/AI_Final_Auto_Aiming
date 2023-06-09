import math

import pyautogui

import numpy as np
import dxcam
import cv2

SCREEN_W = 1920  # screen width, you need to modify this part to fit your own screen
SCREEN_H = 1080  # screen height, you need to modify this part to fit your own screen
SCREEN_CX = SCREEN_W // 2  # screen center x
SCREEN_CY = SCREEN_H // 2  # screen center y
SCREEN_C = [SCREEN_CX, SCREEN_CY]  # screen center position vector
# SCREENSHOT_W = 960  # screenshot width
# SCREENSHOT_H = 960  # screenshot height
SCREENSHOT_W = SCREEN_W
SCREENSHOT_H = SCREEN_H
LEFT = SCREEN_CX - SCREENSHOT_W // 2  # top left corner of detecting frame.x
TOP = SCREEN_CY - SCREENSHOT_H // 2  # top left corner of detecting frame.y
camera = dxcam.create()

def ScreenShout():
    """
    :return: (h,w,c)
    """
    # img = pyautogui.screenshot(region=[LEFT, TOP, SCREENSHOT_W, SCREENSHOT_H])
    img = camera.grab(region=(LEFT, TOP, LEFT+SCREENSHOT_W, TOP+SCREENSHOT_H))
    return np.array(img)


def Center(p):
    """
    :param p: [lx,ly,w,h]
    :return: [x,y] (Center coordinate)
    """
    return [p[0] + p[2] // 2, p[1] + p[3] // 2]


def Distence(a, b):
    """
    :param a: (xa,ya)
    :param b: (xb,yb)
    :return: sqrt((xa-xb)**2 + (yb-ya)**2)
    """
    return math.sqrt(
        ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))


def FindBestCenter(detections):
    """
    :return: best center
    """
    # p: position, d: distance from the center, c: confidence
    cp = {'p': [0, 0, 0, 0], 'd': float('inf'), 'c': 0.0}
    for dt in detections:

        # choose the nearest person
        # from the boxes whose confidence > 0.25
        if dt['conf'] > 0.25:  
            dt_p = dt['position']  
            dt_c = Center(dt_p)  # w,h

            if dt['class'] == 'person': 
                dt_d = Distence(dt_c, SCREEN_C)
                if dt_d < cp['d']:
                    cp['p'] = dt['position']
                    cp['d'] = dt_d
                    cp['c'] = dt['conf']
                    pass

    if cp['d'] < float('inf'):  
        btp = cp['p']  # best target position
        btc = Center(btp)  # best target center
        return btc, btp
    return None, None
