import cv2
import os
from os import listdir
from os.path import isfile, join

#make out put directory (images)
if not os.path.exists('images'):
    os.makedirs('images')

#path to out dir
outDir="images/"

# create way to look into video dir and select video
entries = os.listdir('videos/')
print("----Slicer Script----")
print("Note: Before ypu begin, please place files into the VIDEOS dir for slicing.")
count=1
for entry in entries:
	print(str(count)+":"+entry)
	count=count+1
choice = input("Select which file you want sliced: ")
refChoice= int(choice)-1
videoInput = entries[refChoice]
print(videoInput)
#slice video into jpg files

vidcap = cv2.VideoCapture("videos/"+str(videoInput))
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(outDir+str(count)+"-frame.jpg", image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1