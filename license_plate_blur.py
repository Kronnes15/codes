import cv2
import matplotlib.pyplot as plt
import numpy as np
def read_img(img):
  img3=cv2.imread('/content/car_plate.jpg')
read_img(img3)
plate_cascade=cv2.CascadeClassifier('/content/haarcascade_russian_plate_number.xml')
def plate_detection(img):
  plate_img=img3.copy()
  roi=img3.copy()
  plate_rects=plate_cascade.detectMultiScale(plate_img,scaleFactor = 1.2,minNeighbors=5)
  for (x, y, w, h) in plate_rects:
    roi=roi[y:y+h, x:x+w]
    blurred_roi=cv2.blur( roi,(13, 13))
    img3[y:y+h, x:x+w]=blurred_roi
  return plate_img
result=plate_detection(img3)
   