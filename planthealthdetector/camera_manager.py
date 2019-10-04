# Joel Godinez
# 3 October 2019
# Script to convert images captured to OpenCV compatible

import cv2
import time
import picamera
import numpy as np 
import datetime


def capture_OpenCV_compatible_image():
	""" captures image to an OpenCV object 
	using planar bgr format and reshaping it"""

	with picamera.PiCamera() as camera:
		camera.resolution = (320, 240)
		camera.framerate = 24
		time.sleep(2)
		firstImage = np.empty((240 * 320 * 3,), dtype = np.uint8)
		camera.capture(image, 'bgr')
		image = image.reshape((240, 320, 3))

capture_OpenCV_compatible_image()
print("Call to capture_OpenCV_compatible_image() done")