# test noir v2.1 camera module
# 3 Oct 2019
# Joel Godinez
#

# tell boot loader which python environment we are using
#! /usr/bin/env python 


from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(50)
camera.stop_preview()

# optional rotation statements
#camera.rotation = 180

# optional translucent output for debugging
#camera.start_preview(alpha=200)

