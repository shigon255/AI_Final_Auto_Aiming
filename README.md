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

### Setting
+ Some parameters(Screen size, ...) should be modified to fit your own device. You can modify them in utils/FPSUtils.py in each directories.
+ There're also some parameter that might affect the accuracy of the system. Detail of parameters will be described below.

## How to control
+ Press W key, your mouse will move to the detected object on images automatically.
+ Press R key, your mouse in FPS game(Since the mouse position will be at the middle of the screen) will move to the detected object automatically.
+ Press Ctrl + C to terminate the program.

## Models
+ Currently, models of yolov5 and yolov8 by different training hyper parameters is available in "models" directory.
+ For yolov5 and yolov8, you can use default model that is already in each directories, or you can choose different models from "models" or models trained by yourself. Just replace "best.pt" in the yolov5 and yolov8 directory with the model you want.
+ For retinanet, unfortunately,  the size of model is too large to upload to github repo. We provide a [link](https://drive.google.com/drive/folders/19SnXHvO3bah2VFTYwys-7Q9WShWE9VTo?usp=sharing) to google drive that contain every models we train, including retinanet models. You can replace "model_final.pt" in retinanet directory with the model you want. 
  + Please use NYCU account to view the link.

## Parameters

### Training hyper parameters of default models
+ yolov5: yolov5s, epoch 50, batch size 16.
+ yolov8: yolov8n, epoch 100, batch size 16.
+ retinanet: No default model, need to download/train by yourself.

### Model prediction parameters
+ These parameters can be modified in FPSDetect.py.
+ confidence threshold: 0.25
  + Only object that is detected with confidence higher will be selected as candidates.
+ iou: 0.45

### Aiming system parameters
+ Most of the parameters can be modified in utils/FPSUtils.py.
+ Screen parameters
  + Screen width: 1920
  + Screen height: 1080
  + Screenshot size: same as screen size
+ Detection parameters
  + confidence: threshold: 0.25
    + Objects detected with confidence higher than this threshold from candadiates obtained in prediction will be selected.
    + Among these selected objects, object that the nearest from the screen center will be choosed as the best object to move to.
