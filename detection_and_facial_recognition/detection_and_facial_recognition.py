# Source Code - Defend Intelligence
# coding=utf-8
import cv2
import dlib
import PIL.Image
import numpy as np
from imutils import face_utils
import argparse
from pathlib import Path
import os
import ntpath
import time
import random

parser = argparse.ArgumentParser(description='Easy Facial Recognition App')
parser.add_argument('-i', '--input', type=str, required=True, help='directory of input known faces')

print('[INFO] Starting System...')
print('[INFO] Importing pretrained model..')
pose_predictor_68_point = dlib.shape_predictor("pretrained_model/shape_predictor_68_face_landmarks.dat")
#pose_predictor_5_point = dlib.shape_predictor("pretrained_model/shape_predictor_5_face_landmarks.dat")
face_encoder = dlib.face_recognition_model_v1("pretrained_model/dlib_face_recognition_resnet_model_v1.dat")
face_detector = dlib.get_frontal_face_detector()
print('[INFO] Importing pretrained model..')


    
def transform(self,image, face_locations):
    coord_faces = []
    for face in face_locations:
        rect = face.top(), face.right(), face.bottom(), face.left()
        coord_face = max(rect[0], 0), min(rect[1], image.shape[1]), min(rect[2], image.shape[0]), max(rect[3], 0)
        coord_faces.append(coord_face)
    return coord_faces


def encode_face(self,image):
    face_locations = face_detector(image, 1) # détecte les positions de l'ensemble des visages sur l'image et renvoie cela dans un tab (face_locations)   
    face_encodings_list = []
    landmarks_list = []
    for face_location in face_locations:
        # DETECT FACES
        shape = pose_predictor_68_point(image, face_location) # détecte l'ensemble des 68 points sur le visage concerné
        face_encodings_list.append(np.array(face_encoder.compute_face_descriptor(image, shape, num_jitters=1))) # enregistre dans un tableau le visage encodé à partir du model pré-entrainé de reconnaissance faciale
        # GET LANDMARKS
        shape = face_utils.shape_to_np(shape)
        landmarks_list.append(shape)
    face_locations = transform(image, face_locations)
    return face_encodings_list, face_locations, landmarks_list


def easy_face_reco(self,frame, known_face_encodings, known_face_names):  # fait la comparaison des visages stockés en BD et ceux récupérés en entrée
    rgb_small_frame = frame[:, :, ::-1]
    # ENCODING FACE
    face_encodings_list, face_locations_list, landmarks_list = encode_face(rgb_small_frame) # détecte les positions, détecte l'ensemble des 68 points et enregistre dans un tableau l'ensemble des visages encodés du frame 
    face_names = []
    for face_encoding in face_encodings_list:
        if len(face_encoding) == 0:
            return np.empty((0))
        # CHECK DISTANCE BETWEEN KNOWN FACES AND FACES DETECTED
        vectors = np.linalg.norm(known_face_encodings - face_encoding, axis=1)
        tolerance = 0.5 
        result = []
        for vector in vectors:
            if vector <= tolerance:
                result.append(True)
            else:
                result.append(False)
        if True in result:
            first_match_index = result.index(True) # partie ouverture de la sérrure automatique à rajouter
            name = known_face_names[first_match_index]
        else:
            cv2.imwrite("test.png", frame)
            name = "Unknown_visage"  # partie interaction avec le propriétaire à rajouter et ouverture ou non de la sérrure
        face_names.append(name)

    for (top, right, bottom, left), name in zip(face_locations_list, face_names):  # dessine le cadre en vert et écrit en dessous le nom du visage (s'il est connu) ou visage non connu dans le cas contraire
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 30), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name, (left + 2, bottom - 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

    #for shape in landmarks_list: # marque les points sur les visages détectés
    #    for (x, y) in shape:
    #        cv2.circle(frame, (x, y), 1, (255, 0, 255), -1)

def return_infrarouge(self):
    #return random.choice([0,1])
    return random.randint(1, 100)

if __name__ == '__main__':
    args = parser.parse_args()

    print('[INFO] Importing faces...')
    face_to_encode_path = Path(args.input)
    files = [file_ for file_ in face_to_encode_path.rglob('*.jpg')]

    for file_ in face_to_encode_path.rglob('*.png'):
        files.append(file_)
    if len(files)==0:
        raise ValueError('No faces detect in the directory: {}'.format(face_to_encode_path))
    known_face_names = [os.path.splitext(ntpath.basename(file_))[0] for file_ in files] #  on charge dans un tab l'ensemble des noms des différentes images en BD ouvert sous forme de files

    known_face_encodings = []
    for file_ in files:
        image = PIL.Image.open(file_)  #  on charge dans un tab l'ensemble des images/visages en BD à partir des différents files traités à l'aide de la library pillow
        image = np.array(image)
        face_encoded = encode_face(image)[0][0]
        known_face_encodings.append(face_encoded)   #  on charge dans un tab l'ensemble des visages de la BD encodés

    print('[INFO] Faces well imported')
    print('[INFO] Starting Webcam...') # qui sera déclenché pour notre cas par le OK du capteur infrarouge (webcam = picam pour nous) 
    video_capture = cv2.VideoCapture(0)
    print('[INFO] Webcam well started')
    print('[INFO] Start detecting...') 
    while True:
        var_infrarouge = return_infrarouge()
        if var_infrarouge <= 80:
            ret, frame = video_capture.read()
            easy_face_reco(frame, known_face_encodings, known_face_names)
            cv2.imshow('Easy Facial Recognition App', frame) # to display an image in a window
            #if cv2.waitKey(1):  # 
            #    time.sleep(10)
            #    break
            #time.sleep(5)
            #break
            if cv2.waitKey(1) & 0xFF == ord('q'):  # pour avoir une vision en continue
                break  
        else:
            break
    print('[INFO] Stopping System')  # mettre un wait de x secondes avant stopping system pour arrêter la picam après
    video_capture.release() 
    cv2.destroyAllWindows()
