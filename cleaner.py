import os
import shutil
import glob

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


# known_faces
folder = 'known_faces/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


#unknown_faces
filelist = [ f for f in os.listdir(unknown_faces) if f.endswith(".jpg") ]
for f in filelist:
    os.remove(os.path.join(unknown_faces, f))





    

