import random
import time
from threading import Thread
from FPSDetect import *
from ctypes import *
from utils.FPSUtils import *
import win32api
import threading
import utils.ghub_mouse as ghub
import traceback
from PIL import Image
import pynput
# from MyListener import listen_key, listen_mouse, get_S_L, Mouse_redirection, Move_Mouse
# VK_W = 0x06
# VK_R = 0x52

lock_mode = False
lock_button = eval('pynput.mouse.Button.' + 'x2')
# Start listen the right mouse button and the esc

def on_click(x,y,button,is_press):
    global lock_mode
    if button == lock_button:
        if is_press:
            lock_mode = True
            print("lock")
        else:
            lock_mode = False
            print("lock off")

"""
def shoot_screen():
    while True: 
        img = pyautogui.screenshot(region=[LEFT, TOP, 640, 640])  # take screenshot, input: (left, top, w, h)
        images_path = 'images/'
        img.save(
            images_path + str(int(time.time())) + ''.join(
                random.sample('zyxwvutsrqponmlkjihgfedcba', 2)) + '.jpg')  # generate file name randomly
        time.sleep(0.5)
"""

def listeners():
    listener = pynput.mouse.Listener(on_click=on_click)
    listener.start()
    print("listening")
    listener.join()

if __name__ == '__main__':
    print("Initialize")
    try:
        init()
    except Exception as e:
        print("Initialization error!")
        print("Error: " + str(e))
        traceback.print_exc()
    img = None
    process1 = Thread(
        target=listeners,
    )
    process1.start()
    while True:
        try:
            # Start_detection, Listen = get_S_L()
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

            # Find best target center(btc) to move
            t = time.time()
            print("Start finding")
            btc, btp = FindBestCenter(detections)

            print("End finding, it took " + str(time.time() - t) + "s")

            # w_key_state = win32api.GetKeyState(VK_W)
            # r_key_state = win32api.GetKeyState(VK_R)

            print("lockmode: ", lock_mode)
            if btc is not None and lock_mode:
                print("Start moving mouse")
                mouse_x,mouse_y = pyautogui.position()
                windll.user32.mouse_event(c_uint(0x0001),c_uint(LEFT+btc[0]-mouse_x),c_uint(TOP+btc[1]-mouse_y),c_uint(0x0001),c_uint(0x0001))

            print("----------------------\n")
        except KeyboardInterrupt as e:
            print("keyboard interrupt")
            break
        except IndexError as e:
            print("Index error")
            continue
        except Exception as e:
            print("error image: ", img)
            print("error image shape: ", img.shape)
            imgs = Image.fromarray(img)
            imgs.save("Fault.jpg") 
            print('Error: ' + str(e))
            traceback.print_exc()
            break
    print("program finish")