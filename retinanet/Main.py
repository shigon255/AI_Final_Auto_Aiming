import random
import time

from FPSDetect import *
from ctypes import *
from utils.FPSUtils import *
import os
import cv2

def shoot_screen():
    while True:
        img = pyautogui.screenshot(region=[LEFT, TOP, 640, 640])  # take screenshot, input: (left, top, w, h)
        # path to save screenshots
        images_path = 'images/'
        img.save(
            images_path + str(int(time.time())) + ''.join(
                random.sample('zyxwvutsrqponmlkjihgfedcba', 2)) + '.jpg')  # generate file name randomly
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        init()
    except Exception as e:
        print("Initialization error!")
        print("Error: "+str(e))
    while True:
        try:
            img = ScreenShout() 
            detections = detect(img)
            print("start move")
            btc, btp = FindBestCenter(detections)

            print("detection: ")
            print(detections)
            
            if btc is not None:
              print("Coordinate: ", int(LEFT + btc[0]), int(TOP + btc[1]))
              pyautogui.moveTo(int(LEFT + btc[0]), int(TOP + btc[1]))
            
        except Exception as e:
            print('ERROR!')
            print('Error: '+ str(e))
            break
