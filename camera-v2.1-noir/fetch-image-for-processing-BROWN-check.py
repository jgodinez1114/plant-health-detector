#Joel Godinez
#4 October 2019
#Plant Health Detector

import cv2
import time
import picamera
import re
import numpy as np

def fetchImageForProcessing():
    #read in an file from local directory
    file1 = cv2.imread("piImage1.jpg")

    #optional: show image which was fetched
    #cv2.imshow("myImage",file1)
    
    return file1

def detectForBlue(myImageMatrix):
    """ Arg: take in an image file for processing
        check the image against set threshold values for Blue """


    #create 2 arrays with threshold values (MAT objects or vectors can be used in cpp)
    #these values correspond to blue. Blue detection ocurring here.
    lowerThreshBlue = np.array([100,50,50]) #initial values: 110,0,0
    upperThreshBlue = np.array([140,255,255]) #initial values 130,0,0

    #note: hues correspond to a circular(360 degree) mapping

    #change BGR to HSV
    moddedImage = cv2.cvtColor(myImageMatrix, cv2.COLOR_BGR2HSV)

    #show the color detection in a mask by showing the pixels as white where detection occured(black elsewhere)
    mask = cv2.inRange(moddedImage, lowerThreshBlue, upperThreshBlue)

    #KEY STEP: see if region of white pixels exits BEFORE bitwise ANDing

    #bitwise AND to extract the targeted color in detected areas
    extractedRegion = cv2.bitwise_and(moddedImage,moddedImage,mask = mask)

    #show the resulting mask
    cv2.imshow("Extracted Blue Region", extractedRegion)
    #wait until windows are closed by user
    cv2.waitKey(0)

def detectForBrown(myImageMatrix):
    """ Arg: take in an image file for processing
        check the image against set threshold values for Brown color """
    

    #these values correspond to brown. Brown detection occuring here
    lowerThreshBrown = np.array([10, 50, 50 ])    #initial values:5,50,50
    upperThreshBrown = np.array([20, 255, 255]) #initial values:45,255,255


    # note: hues corrspond to a circular(360 degree) mapping
    
    # change BGR to HSV
    moddedImage = cv2.cvtColor(myImageMatrix, cv2.COLOR_BGR2HSV)
    
    #show the color detection in a mask by showing the pixels as white where detection occured(black elsewhere) 
    mask = cv2.inRange(moddedImage, lowerThreshBrown, upperThreshBrown)
    
    #KEY STEP: see if region of white pixels exist BEFORE  bitwise ANDing 
    
    #bitwise AND to extract the targeted color in detected areas
    extractedRegion = cv2.bitwise_and(moddedImage,moddedImage,mask = mask)
    # show the mask
    cv2.imshow("Extracted Brwon Region", extractedRegion)
    #wait until window is closed by user
    cv2.waitKey(0)
    
    # create a MAT with blue==255, all others==0
    
    #imshow the image at this point
    
    #take the 1st pixel value and subtract and add 10 to it
    
    # lower threshold == 220 && upper threshold at 240    
    
    
    # ToDo: comparison traversal of pixels for brown spotting stages of severity


myImageMatrix = fetchImageForProcessing()
cv2.imshow("My raw image matrix.",myImageMatrix)
#detectForBrown(myImageMatrix)
detectForBlue(myImageMatrix)


    
    