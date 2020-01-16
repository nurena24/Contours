import cv2
import numpy as np
#https://stackoverflow.com/questions/55169645/square-detection-in-image

image = cv2.imread('bowed.jpg')
image = cv2.resize(image, (1920, 1080))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(blur, -1, sharpen_kernel)
thresh = cv2.threshold(sharpen,160,255, cv2.THRESH_BINARY_INV)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

min_area = 1400
max_area = 47681.5
image_number = 0
for c in cnts:
    area = cv2.contourArea(c)
    print(area)
    if area > min_area and area < max_area:
        x,y,w,h = cv2.boundingRect(c)
        print(x)
        print(y)
        print(w)
        print(h)
        ROI = image[y:y+(h+50), x:x+(w+50)]
        cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2) #superimposed rectaqnge on original image
        cv2.imwrite('ROI_{}.png'.format(image_number), ROI)  # Writes original image crop to file
        image_number += 1

cv2.imshow('sharpen', sharpen)
cv2.imshow('close', close)
cv2.imshow('thresh', thresh)
cv2.imshow('image', image)
cv2.waitKey()