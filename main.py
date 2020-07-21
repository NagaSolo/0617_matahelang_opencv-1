import cv2 as cv
from cv2 import VideoCapture
import numpy as np

# checking installation status & version of module
print(f'Version number is {cv.__version__} ')

# pass int 0 for first camera on our device
cap = VideoCapture('test/shesgone.mp4')
program_masih_berjalan = True
while program_masih_berjalan:
  if (cap.isOpened() == False):
    print('Error opening camera')
    break
  elif (cap.isOpened() == True):
    # frame by frame capture
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
      print("Can't receive frame (stream end?). Exiting ...")
      break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
      cap.release()
      cv.destroyAllWindows()
      break


