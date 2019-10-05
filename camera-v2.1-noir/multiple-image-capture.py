# 4 Oct 2019
# Joel Godinez

import time
import picamera

with picamera.PiCamera() as camera:
    # capture High Definition image
    camera.resolution = (1024, 768)
    #camera.start_preview()
    # Camera warm-up time
    time.sleep(2)

    # name the files in the order they were captured
    for img in range(5):
        imageName="healthyImage"+str(img+1)+".jpg"
        camera.capture(imageName)
    #camera.stop_preview()
