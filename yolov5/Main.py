import random
import time

from FPSDetect import *
from ctypes import *
from utils.FPSUtils import *
import win32api
import threading
import utils.ghub_mouse as ghub
import traceback

VK_W = 0x57
VK_R = 0x52

"""
pressed = False
keyboard_terminate = threading.Event()
btc = None
btp = None
# target_pos = SCREEN_C

def monitor_keyboard():
    global pressed
    global keyboard_terminate
    global btc
    global btp
    # global target_pos
    while not keyboard_terminate.is_set():
        w_key_state = win32api.GetKeyState(VK_W)
        r_key_state = win32api.GetKeyState(VK_R)
        # pressed = w_key_state < 0
        if btc is not None and (w_key_state < 0 or r_key_state < 0):# if w key is pressed -> for image detection
            # print("Coordinate: ", int(LEFT + btc[0]), int(TOP + btc[1]))
            # pyautogui.moveTo(int(LEFT + btc[0]), int(TOP + btc[1]))
            # windll.user32.SetCursorPos(int(LEFT + btc[0]), int(TOP + btc[1]))
            # print("\ntarget pos", target_pos)
            # current_cursor_pos = win32api.GetCursorPos()
            # print("current cursor pos: ", current_cursor_pos)
            # move_vector = [target_pos[0] - current_cursor_pos[0], target_pos[1] - current_cursor_pos[1]]
            # print("move vector: ", move_vector)
            # ghub.mouse_xy(int(move_vector[0]/2.6), int(move_vector[1]/2.6))
            ghub.mouse_xy(int(btc[0] - (SCREEN_W // 2)),int(btc[1] - (SCREEN_H - (btp[3] // 2))))
            btc = None
            btp = None
            print("current Pos after moving: ", win32api.GetCursorPos())
            print("")
            if r_key_state < 0:
                target_pos = SCREEN_C
            else:
                target_pos = int(LEFT + btc[0]), int(TOP + btc[1])
    print("keyboard interrupt in keyboard thread")
"""
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
    # keyboard_thread = threading.Thread(target=monitor_keyboard)
    # keyboard_thread.start()
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
                # if btc is not None:
                  #   target_pos = int(LEFT + btc[0]), int(TOP + btc[1])
                print("End finding, it took " + str(time.time() - t) + "s")

                w_key_state = win32api.GetKeyState(VK_W)
                r_key_state = win32api.GetKeyState(VK_R)
                if btc is not None and (w_key_state < 0 or r_key_state < 0):
                    print("Start moving mouse")
                    if r_key_state < 0:
                        ghub.mouse_xy(int(btc[0] - (SCREEN_W // 2)),int(btc[1] - (SCREEN_H - (btp[3] // 2))))
                    else:
                        pyautogui.moveTo(int(LEFT + btc[0]), int(TOP + btc[1]))
                    print("End moving mouse")
                print("----------------------\n")
            except Exception as e:
                print('Error: ' + str(e))
                traceback.print_exc()
                break
        raise KeyboardInterrupt
    except KeyboardInterrupt as e:
        # keyboard_terminate.set()
        print("keyboard interrupt in main thread")

    # keyboard_thread.join()
    print("program finish")