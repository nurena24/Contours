import numpy as np
#https://stackoverflow.com/questions/11424002/how-to-detect-simple-geometric-shapes-using-opencv
import cv2

img = cv2.imread('slabonly.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,100,255,1)

contours,h = cv2.findContours(thresh,1,2)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print(len(approx))
    if len(approx)==5:
        print("pentagon")
        cv2.drawContours(img,[cnt],0,255,-1)
    elif len(approx)==3:
        print("triangle")
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        print("square")
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
    elif len(approx) == 2:
        print("rectangle")
        cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
    elif len(approx) == 9:
        print("half-circle")
        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    elif len(approx) > 15:
        print("circle")
        cv2.drawContours(img,[cnt],0,(0,255,255),-1)

image_resized = cv2.resize(img, (1920, 1080))
cv2.imshow('img',image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()