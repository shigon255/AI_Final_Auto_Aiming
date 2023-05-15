import random
import time

from FPSDetect import *
from ctypes import *
from utils.FPSUtils import *
import os
import cv2


# dll = cdll.LoadLibrary(r'lib/Dll.dll')  # 加載用C語言封裝過的易鍵鼠dll


def shoot_screen():
    while True:
        img = pyautogui.screenshot(region=[LEFT, TOP, 640, 640])  # region為螢幕擷取區域，格式為(left, top, w, h)
        # 儲存遊戲過程中的截圖的路徑
        images_path = 'images/'
        img.save(
            images_path + str(int(time.time())) + ''.join(
                random.sample('zyxwvutsrqponmlkjihgfedcba', 2)) + '.jpg')  # 隨機生成文件名
        time.sleep(0.5)

if __name__ == "__main__":
    # ssp = Process(target=shoot_screen, name="ssp", args=())
    # ssp.start()
    # mPid = PID(0, 0, 1.0, 0)  # PID控制器參數: (真直, p, i, d)(有問題)

    while True:
        try:
            img = ScreenShout()  # 擷取螢幕檢測區域
            detections = detect(img)  # 送入yolo檢測
            print("start move")
            btc, btp = FindBestCenter(detections)  # 確定目標最優的射擊中心

            print("detection: ")
            print(detections)
            
            if btc is not None:  # 如果螢幕區域有射擊目標
              #   dll.MoveTo2(int(LEFT + btc[0]), int(TOP + btc[1]))  # 調用易鍵鼠移動滑鼠(此處更換為自己的)
              print("Coordinate: ", int(LEFT + btc[0]), int(TOP + btc[1]))
              pyautogui.moveTo(int(LEFT + btc[0]), int(TOP + btc[1]))
            
        except Exception as e:
            print('ERROR!')
            print('Error: '+ str(e))
            break
