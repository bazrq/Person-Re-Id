#this file is to connect all the subfiles to run the program
#------------------------------------------------------------#
import os
import os
import shutil
import glob


#1 

os.system('python slicer.py')
os.system('python data_generator.py')
os.system('python face_extractor.py')
os.system('python face_clusters.py')

# After succesfull run, del unwanted files.

images = "./images/"
updated_images= "./updated_images/"
faces = "./faces/"
known_faces = "./known_faces/"
unknown_faces = "./unknown_faces/"
dirs = [images, updated_images, faces, known_faces, unknown_faces]

# images
filelist = [ f for f in os.listdir(images) if f.endswith(".jpg") ]
for f in filelist:
    os.remove(os.path.join(images, f))

# updated_images
filelist = [ f for f in os.listdir(updated_images) if f.endswith(".jpg") ]
for f in filelist:
    os.remove(os.path.join(updated_images, f))

# faces
filelist = [ f for f in os.listdir(faces) if f.endswith(".jpg") ]
for f in filelist:
    os.remove(os.path.join(faces, f))

#unknown_faces
filelist = [ f for f in os.listdir(unknown_faces) if f.endswith(".jpg") ]
for f in filelist:
    os.remove(os.path.join(unknown_faces, f))