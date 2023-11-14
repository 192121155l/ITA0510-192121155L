import cv2
import numpy as np
input_image = cv2.imread("C:/Users/P Leela Mohan/Desktop/computer vision/Picture1.jpg", 100)  
edges = cv2.Canny(input_image, threshold1=100, threshold2=200)  
cv2.imshow('Original Image', input_image)
cv2.imshow('Edge-detected Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
