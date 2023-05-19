# AI_Final_Auto_Aiming
+ This is the repo of our final project. The aim of this project is to test different model's performance on auto aiming in FPS game
+ The Auto aiming part is from [this project](https://github.com/chaoyu1999/FPSAutomaticAiming)


# Usage
## Run the program
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

## Open/Close the aiming system
+ Press "W" key to activate the aiming system, the mouse will move to the target automatically as long as there is any target on the screen
+ Press Ctrl + C to terminate the program

## Current model's training hyper parameter
+ yolov5: yolov5s, epoch 50, batch size 16
+ yolov8: yolov8n, epoch 100, batch size 16
+ retinanet: Need to download/train by yourself(Since it's too big to upload to github)