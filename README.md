# AI_Final_Auto_Aiming
+ This is the repo of our final project. The aim of this project is to test different model's performance on auto aiming in FPS game
+ The Auto aiming part is from [this project](https://github.com/chaoyu1999/FPSAutomaticAiming)


# Usage
## Setup & Activate the program
### yolov5 & yolov8
+ build environment from yolo_environment.yml
+ clone the repo
+ cd yolov5/yolov8
+ python Main.py

### retinanet
+ build environment from retinanet_environment.yml
+ clone the repo
+ cd retinanet
+ Name your trained model "model_final.pt" and put it in retinanet
+ python Main.py

## How to control
+ Press W key to move your mouse to the detect object on images
+ Press R key to move your mouse in FPS game(Since the mouse position will be at the middle of the screen)
+ Press Ctrl + C to terminate the program


## Current model's training hyper parameter
+ yolov5: yolov5s, epoch 50, batch size 16
+ yolov8: yolov8n, epoch 100, batch size 16
+ retinanet: Need to download/train by yourself(Since it's too big to upload to github)
