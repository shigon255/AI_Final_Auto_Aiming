import random
import time

from FPSDetect import *
from ctypes import *
from utils.FPSUtils import *
import win32api
import threading
import os
import cv2

VK_LBUTTON = 0x01
VK_W = 0x57

pressed = False
keyboard_terminate = threading.Event()
btc = None

def monitor_keyboard():
    global pressed
    global keyboard_terminate
    global btc
    while not keyboard_terminate.is_set():
        w_key_state = win32api.GetKeyState(VK_W)
        pressed = w_key_state < 0
        if btc is not None and w_key_state < 0:# if the left mouse button is pressed
            print("Coordinate: ", int(LEFT + btc[0]), int(TOP + btc[1]))
            pyautogui.moveTo(int(LEFT + btc[0]), int(TOP + btc[1]))
    print("keyboard interrupt in keyboard thread")

def shoot_screen():
    while True:
        img = pyautogui.screenshot(region=[LEFT, TOP, 640, 640])  # take screenshot, input: (left, top, w, h)
        images_path = 'images/'
        img.save(
            images_path + str(int(time.time())) + ''.join(
                random.sample('zyxwvutsrqponmlkjihgfedcba', 2)) + '.jpg')  # generate file name randomly
        time.sleep(0.5)

if __name__ == '__main__':
    print("Initialize")
    keyboard_thread = threading.Thread(target=monitor_keyboard)
    keyboard_thread.start()
    try:
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
                print("Start finding")
                btc, btp = FindBestCenter(detections)
                print("End finding, it took " + str(time.time() - t) + "s")

                print("----------------------\n")
            except:
                break
        raise
    except Exception as e:
        print('ERROR!')
        print('Error: '+ str(e))
        keyboard_terminate.set()
        print("keyboard interrupt in main thread")

    keyboard_thread.join()
    print("program finish")