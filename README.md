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
Build Database:
1. Slice video feed into images. run slicer.py and select any mp4 of your choice. 
NOTE: Video dir must be made.
3. Run data_generator.py to draw bounding boxes around every face in step 1.
4. Run face_extractor.py to crop faces and save them in unknown_faces dir.
5. Run face_clusters.py to cluster all faces in unknown_faces dir, and make database.

Find Missing People:
1. Clear the unknown_faces dir.
2. Slice video feed into images. run slicer.py and select any mp4 of your choice.
3. Run data_generator.py to draw bounding boxes around every face in step 2.
4. Run face_extractor.py to crop faces and save them in unknown_faces dir.
5. Run re-id.py to see if there is a match for unknown_faces and anyone in known_faces

# Citations
This project and its code is sourced from open source software. 
Please visit the following Github page and website, as the work done there heavily allowed us to 
complete this task. 

https://pythonprogramming.net/facial-recognition-python/

https://pythonprogramming.net/facial-recognition-python/












