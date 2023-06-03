# AI_Final_Auto_Aiming
+ This is the repo of our final project of Intro. to AI, Spring 2023. The aim of this project is to test different model's performance on auto aiming in FPS game.
+ We choose to train models that can be used in game "Apex legend".
+ We try 3 different models: [yolov5](https://github.com/ultralytics/yolov5), [yolov8](https://github.com/ultralytics/ultralytics) and retinanet.
+ The implementation of retinanet on pytorch is from [this project](https://github.com/yhenon/pytorch-retinanet).
+ The Auto aiming part is from [this project](https://github.com/chaoyu1999/FPSAutomaticAiming).
+ We trained our models by [this dataset](https://github.com/goldjee/AL-YOLO-dataset).
+ This project is only for education and research purpose. Using this project in real game might make your account be banned. Please take your own risk.


# Usage
## Setup & Execute the program
### yolov5 & yolov8
+ build environment from yolo_environment.yml
+ clone the repo
+ cd yolov5/yolov8
+ python Main.py

### retinanet
+ build environment from retinanet_environment.yml
+ clone the repo
+ cd retinanet
+ Name your trained model "model_final.pt" and put it in retinanet directory
+ python Main.py

## How to control
+ Press W key, your mouse will move to the detected object on images automatically.
+ Press R key, your mouse in FPS game(Since the mouse position will be at the middle of the screen) will move to the detected object automatically.
+ Press Ctrl + C to terminate the program.

## Models
+ Currently, models of yolov5 and yolov8 by different training hyper parameters is available in "models" directory
+ For yolov5 and yolov8, you can use default model that is already in each directories, or you can choose different models from "models" or models trained by yourself. Just replace "best.pt" in the yolov5 and yolov8 directory with the model you want.
+ For retinanet, unfortunately,  the size of model is too large to upload to github repo. We provide a [link](https://drive.google.com/drive/folders/19SnXHvO3bah2VFTYwys-7Q9WShWE9VTo?usp=sharing) to google drive that contain every models we train, including retinanet models. You can replace "model_final.pt" in retinanet directory with the model you want.

## Training hyper parameters of default model
+ yolov5: yolov5s, epoch 50, batch size 16.
+ yolov8: yolov8n, epoch 100, batch size 16.
+ retinanet: No default model, need to download/train by yourself.
