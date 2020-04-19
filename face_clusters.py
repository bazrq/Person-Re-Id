from pyfacy import face_clust
mdl = face_clust.Face_Clust_Algorithm('./faces')
mdl.load_faces()
mdl.save_faces('./known_faces')