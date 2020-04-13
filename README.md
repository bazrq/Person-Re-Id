# Person-Re-Id
This repo is to house code and knowledge base to complete the problem of Person Re-Identification, which was chosen as a final year engineering project.

# Requirements
- linux (preferably)
- Windows

Install the requirements file and do the following:
- sudo pip3.7 install --upgrade numpy scipy
- sudo apt-get update && sudo apt-get -y install git cmake
- sudo pip install --upgrade Click Pillow
- sudo pip install dlib
- pip install git+https://github.com/ageitgey/face_recognition
- pip install git+https://github.com/ageitgey/face_recognition_models

# Start-up
Before we do anything, we must make a folder in known_faces for anyone we want to find. After making a folder for said person
we must then add front shot images with variation to that person. Now you are ready to go, follow the instructions:

1. Slice video feed into .JPG files by editing the slicer.py file -> vidcap = cv2.VideoCapture("./vidoes/*SOMEVIDEO*.mp4")
2. run data_generator.py
3. run face_extractor.py
4. run re-id.py











