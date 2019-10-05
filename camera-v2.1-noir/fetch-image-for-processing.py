#Joel Godinez
#4 October 2019
#Plant Health Detector

import cv2
import time
import picamera
import re
import numpy as np

def fetchImageForProcessing():
    #read in an image file
    file1 = cv2.imread("NEWnewImage1.jpg")
    #optional: show image which was fetched
    #cv2.imshow("myImage",file1)
    
    return file1

def detectForBlue(myImageMatrix):
    """ Arg: take in an image file for processing
        check the image against set threshold values """
    #create 2 arrays with threshold values (MAT objects or vectors can be used in cpp)
    #these values correspond to blue. Blue detection occuring here
    lowerThreshBlue = np.array([110, 50, 50 ])    #initial values:110,0,0
    upperThreshBlue = np.array([130, 255, 255]) #initial values:130,0,0
    # note: hues corrspond to a circular(360 degree) mapping
    
    # change BGR to HSV
    moddedImage = cv2.cvtColor(myImageMatrix, cv2.COLOR_BGR2HSV)
    
    #show the color detection in a mask by showing the pixels as white where detection occured(black elsewhere) 
    mask = cv2.inRange(moddedImage, lowerThresh, upperThresh)
    
    #KEY STEP: see if region of white pixels exist BEFORE  bitwise ANDing 
    
    #bitwise AND to extract the targeted color in detected areas
    extractedRegion = cv2.bitwise_and(moddedImage,moddedImage,mask = mask)
    # show the mask
    cv2.imshow("Extracted Blue Region", extractedRegion)
    cv2.waitKey(0)
    
    # create a MAT with blue==255, all others==0
    
    #imshow the image at this point
    
    #take the 1st pixel value and subtract and add 10 to it
    
    # lower threshold == 220 && upper threshold at 240
    
    
    
    # ToDo: comparison traversal of pixels for brown spotting stages of severity


myImageMatrix = fetchImageForProcessing()
cv2.imshow("my image matrix",myImageMatrix)
detectForBlue(myImageMatrix)


    
    