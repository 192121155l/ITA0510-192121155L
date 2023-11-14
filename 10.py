import cv2
import shutil
original_image_path = "C:/Users/P Leela Mohan/Desktop/computer vision/th (1).jpeg"
original_image = cv2.imread(original_image_path)
resized_image = cv2.resize(original_image, None, fx=0.5, fy=0.5)
new_image_path ="C:/Users/P Leela Mohan/Desktop/computer vision/th.jpeg"
cv2.imwrite(new_image_path, resized_image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)  
cv2.destroyAllWindows()  
destination_path = "C:/Users/P Leela Mohan/Desktop/computer vision/th.jpeg"
shutil.move(original_image_path, destination_path)
