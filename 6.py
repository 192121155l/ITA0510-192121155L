import cv2
import numpy as np
cap = cv2.VideoCapture("C:/Users/P Leela Mohan/Videos/WhatsApp Video 2023-05-13 at 10.05.41.mp4")
if (cap.isOpened()== False):
          Print("Error opening video file")
while(cap.isOpened()):
          ret, frame = cap.read()
          if ret == True:
              cv2.imshow('Frame', frame)
              if cv2.waitKey(250) & 0xFF == ord('q'):
                         break
          else:
                 break
cap.release()
cv2.destroyAllWindows()
