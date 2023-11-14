import cv2
import numpy as np
image_path ="C:/Users/P Leela Mohan/Desktop/computer vision/Picture2.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
cv2.imshow("original image",image)
cv2.waitKey(0)
kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(image, kernel, iterations=1)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows
