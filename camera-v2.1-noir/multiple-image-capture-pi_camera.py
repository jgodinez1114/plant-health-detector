# 8 Oct 2019
# Joel Godinez

import time
import picamera

with picamera.PiCamera() as camera:
	# capture High Defintion image
	camera.resolution = (1024,768)
	
	# Camera warm-up time
	time.sleep(2)

	# name the files in the order they were captured
	for img in range(5):
		imageName = "piImage" + str(img + 1) + ".jpg"
		camera.capture(imageName)

