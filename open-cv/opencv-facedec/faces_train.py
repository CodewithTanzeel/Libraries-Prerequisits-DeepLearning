import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


DIR = r'C:\Users\FATTANI COMPUTERS\OneDrive\Documents\pre-req-Deeplearning\open-cv\opencv-facedec\Faces\train'

# Derive people from the subfolders inside DIR. This avoids mismatches between
# hardcoded names and actual folder names on disk.
if os.path.isdir(DIR):
    people = sorted([d for d in os.listdir(DIR) if os.path.isdir(os.path.join(DIR, d))])
else:
    people = []

# Quick sanity check for the training DIR
if not os.path.isdir(DIR):
    raise SystemExit(f"Training directory does not exist: {DIR}")
    
    

haar_cascade = cv.CascadeClassifier('haar_face.xml')
features =[]
labels =[]


def create_train():
    missing = []
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        if not os.path.isdir(path):
            print(f"Warning: folder for person '{person}' not found at: {path}")
            missing.append(person)
            continue

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)

            if img_array is None:
                print(f"Warning: could not read image (skipping): {img_path}")
                continue

            try:
                gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            except Exception as e:
                print(f"Warning: failed to convert image to gray for {img_path}: {e}")
                continue

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

    if missing:
        print("The following people were missing folders and were skipped:")
        for m in missing:
            print(" -", m)
                
                
create_train()
print('tranning Done ------')
print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')
features = np.array(features,dtype='object')
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('Features.npy',features)
np.save('labels.npy',labels)
