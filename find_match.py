#this file is to connect all the subfiles to run the program
#------------------------------------------------------------#
import os

#1 

os.system('python slicer.py')
os.system('python data_generator.py')
os.system('python face_extractor.py')
os.system('python re-id.py')
