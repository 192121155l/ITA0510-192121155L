import cv2
import numpy as np
# read the input image
img = cv2.imread("C:/Users/P Leela Mohan/Pictures/my pics/IMG-20230602-WA0133.jpg") # access the image height and width
rows,cols,ch = img.shape
# define at three point on input image
pts1 = np.float32([[50,50],[200,50],[50,200]])
# define three points corresponding location to output image pts2 = np.float32([[10,100],[200,50],[100,250]])
# get the affine transformation Matrix M = cv2.getAffineTransform(pts1,pts2)
# apply affine transformation on the input image
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("Affine Transform", dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 
