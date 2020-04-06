import cv2
import os

#make out put directory (images)
if not os.path.exists('images'):
    os.makedirs('images')

#path to dir
outDir="images/"

#slice video into jpg files
vidcap = cv2.VideoCapture("umtitti.mp4")
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(outDir+str(count)+"-frame.jpg", image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1