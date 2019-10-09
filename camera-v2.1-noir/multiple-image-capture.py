# 4 Oct 2019
# Joel Godinez

import time
import picamera
import datetime

with picamera.PiCamera() as camera:
    # capture High Definition image
    camera.resolution = (1024, 768)
    #camera.start_preview()
    # Camera warm-up time
    time.sleep(2)

    # name the files in the order they were captured
    for img in range(5):
        # save the timestamp 
        date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        imageName='/home/pi/plant-health-detector/green-module-files/'+ date +".jpg"
        camera.capture(imageName)
        time.sleep(5)
    #camera.stop_preview()
