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
        images_path = 'images/'
        img.save(
            images_path + str(int(time.time())) + ''.join(
                random.sample('zyxwvutsrqponmlkjihgfedcba', 2)) + '.jpg')  # generate file name randomly
        time.sleep(0.5)

if __name__ == "__main__":
    while True:
        try:
            print("\n----------------------")
            # Take screen shot
            t = time.time()
            print("Start taking screen shot")
            img = ScreenShout() 
            print("End taking screen shot, it took " + str(time.time()-t) + "s")

            # Detection
            t = time.time()
            print("Start detection")
            detections = detect(img)
            print("End detection, it took " + str(time.time()-t) + "s")
            print("detection: ")
            print(detections)

            # Find center to move
            t = time.time()
            print("Start finding & moving")
            btc, btp = FindBestCenter(detections)
            if btc is not None:
              print("Coordinate: ", int(LEFT + btc[0]), int(TOP + btc[1]))
              pyautogui.moveTo(int(LEFT + btc[0]), int(TOP + btc[1]))
            print("End findmoving & moving, it took " + str(time.time() - t) + "s")

            print("----------------------\n")
            
        except Exception as e:
            print('ERROR!')
            print('Error: '+ str(e))
            break
