# AI_Final_Auto_Aiming

## Project Overview
+ This is the repo of our final project of Intro. to AI, Spring 2023. 
+ The aim of this project is to build an automatic aiming system, and test different model's performance on auto aiming in FPS game.
+ We choosed to train models that can be used in game "Apex legend".
+ We tried 3 different models: [yolov5](https://github.com/ultralytics/yolov5), [yolov8](https://github.com/ultralytics/ultralytics) and [retinanet](https://arxiv.org/abs/1708.02002).
+ This project is only for education and research purpose. Using this project in real game might make your account be banned. Please take your own risk.

## Experiment results
+ We conducted experiments on yolov5n, yolov5s, yolov8n, yolov8s, yolov8m, retinanet models
+ All models are trained on the same dataset, with epoch = 50, batch size = 16
+ We evaluate the performance of each models by below 3 indices
  + Average FPS of the aiming system
  + Average time the model take to do single detection 
  + mAP with iou threshold = 0.5
+ Results

|Model |Average time(s)|Average FPS|mAP|
|-----|--------|--------|--------|
|yolov5n|0.00988|39.7632|0.97765|
|yolov5s|0.00977|37.87687|0.98936|
|yolov8n|0.01820|32.91317|0.94717|
|yolov8s|0.01771|35.78728|0.95776|
|yolov8m|0.02174|33.95591|0.96542|
|retinanet|0.04593|10.54922|0.94745|

## Usage
### Setup & Execute the program
+ build environment from environment.yml
+ yolov5 & yolov8
  + clone the repo
  + cd yolov5/yolov8
  + python Main.py
+ retinanet
  + clone the repo  
  + cd retinanet
  + Name your trained model "model_final.pt" and put it in retinanet directory
  + python Main.py

### Setting
+ Some parameters(Screen size, ...) should be modified to fit your own device. You can modify them in utils/FPSUtils.py in each directories.
+ There're also some parameter that might affect the accuracy of the system. Detail of parameters will be described below.

### How to control
+ Click the right mouse button, the mouse will move toward the object(if detected) automatically.
+ Press Ctrl + C to terminate the program.

### Models
+ Currently, models of yolov5 and yolov8 by different training hyper parameters is available in "models" directory.
+ For yolov5 and yolov8, you can use default model that is already in each directories, or you can choose different models from "models" or models trained by yourself. Just replace "best.pt" in the yolov5 and yolov8 directory with the model you want.
+ For retinanet, unfortunately,  the size of model is too large to upload to github repo. We provide a [link](https://drive.google.com/drive/folders/19SnXHvO3bah2VFTYwys-7Q9WShWE9VTo?usp=sharing) to google drive that contain every models we train, including retinanet models. You can replace "model_final.pt" in retinanet directory with the model you want. 
  + Please view the link with NYCU account.

## Parameters

### Training hyper parameters of default models
+ yolov5: yolov5s, epoch 50, batch size 16.
+ yolov8: yolov8n, epoch 50, batch size 16.
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

## (Experimental) TensorRT support
+ In yolov8, we add tensorRT support. You can first transfer yolov8 model into tensorRT model, and change the model name in FPSDetect.py to use tensorRT model to detect.
  + How to transfer model into tensorRT: [TensorRT-For-YOLO-Series](https://github.com/Linaom1214/TensorRT-For-YOLO-Series)
  + Note that you need to prepare environment for executing tensorRT

## Videos
+ [Project representation](https://youtu.be/LWb7hWWDsR8)
+ [Project demo](https://www.youtube.com/watch?v=PdI-JhGfUEU)

## Future work
+ Full TensorRT support
+ Thorough experiments
+ More models

## Reference
+ The implementation of retinanet on pytorch is from [this project](https://github.com/yhenon/pytorch-retinanet).
+ The Auto aiming part is mainly from [this project](https://github.com/chaoyu1999/FPSAutomaticAiming).
+ Part of the implementation is from [this project](https://github.com/Franklin-Zhang0/Yolo-v8-Apex-Aim-assist)
+ We trained our models by [this dataset](https://github.com/goldjee/AL-YOLO-dataset).
