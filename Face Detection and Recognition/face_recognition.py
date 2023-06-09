import os
import cv2 as cv
import numpy as np

# img = cv.imread('Images/man.jpg')
# cv.imshow('Man', img)

people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
p = []

# Please provide your respective path
DIR = r'C:\Users\ashut\Desktop\OpenCV Projects\Face Detection and Recognition\train'
haar_cascade = cv.CascadeClassifier('harr_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_rol = gray[y:y+h, x:x+w]
                features.append(faces_rol)
                labels.append(label)


create_train()
print('Training done ------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

# print(f'length of the features = {len(features)}')
# print(f'length of the labels = {len(labels)}')
            
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer on the features list and labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)


# for i in os.listdir(r'C:\Users\ashut\Desktop\OpenCV Projects\Opencv\Images\train'):
#     p.append(i)

# print(p)

# cv.waitKey(0)