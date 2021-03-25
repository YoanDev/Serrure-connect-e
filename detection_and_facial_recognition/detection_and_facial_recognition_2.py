# Source Code - Defend Intelligence
import cv2
import socket
import numpy as np
import face_recognition
import argparse
from pathlib import Path
import os
import ntpath
import random
import time


parser = argparse.ArgumentParser(description='Easy Facial Recognition App')
parser.add_argument('-i', '--input', type=str, required=True, help='directory of input known faces')


def transform(image, face_locations):
    coord_faces = []
    for face in face_locations:
        rect = face.top(), face.right(), face.bottom(), face.left()
        coord_face = max(rect[0], 0), min(rect[1], image.shape[1]), min(rect[2], image.shape[0]), max(rect[3], 0)
        coord_faces.append(coord_face)
    return coord_faces


def encode_face(image):
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

def EnvoieImage():

        HOST = '172.20.10.3'
        PORT = 12345
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        print('Connexion vers ' + HOST + ':' + str(PORT) + ' reussie.')

        f = open('test.png', 'rb')
        print('Sending...')
        l = f.read(1024)
        while (l):
            print('Sending...')
            client.send(l)
            l = f.read(1024)
            print(len(l))

        client.shutdown(socket.SHUT_WR)

        print('Reception...')
        donnees = client.recv(1024)
        print('Recu :', donnees)

        print('Deconnexion')
        client.close()

def easy_face_reco(frame, known_face_encodings, known_face_names):  # fait la comparaison des visages stockés en BD et ceux récupérés en entrée
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    process_this_frame = True
    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

             # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                 first_match_index = matches.index(True)
                 name = known_face_names[first_match_index]
            else:
                cv2.imwrite("test.png", frame)
                name = "Unknown_visage"  # partie interaction avec le propriétaire à rajouter et ouverture ou non de la sérrure
                #EnvoieImage()

            # Or instead, use the known face with the smallest distance to the new face
            #face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            #best_match_index = np.argmin(face_distances)
            #if matches[best_match_index]:
            #    name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


def return_infrarouge():
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
        image = face_recognition.load_image_file(file_)
        face_encoded = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoded)   #  on charge dans un tab l'ensemble des visages de la BD encodés

    print('[INFO] Faces well imported')
    print('[INFO] Starting Webcam...') # qui sera déclenché pour notre cas par le OK du capteur infrarouge (webcam = picam pour nous) 
    video_capture = cv2.VideoCapture(0)
    print('[INFO] Webcam well started')
    print('[INFO] Start detecting...') 
    while True:
        ret, frame = video_capture.read()
        easy_face_reco(frame, known_face_encodings, known_face_names)
        cv2.imshow('Easy Facial Recognition App', frame) # to display an image in a window

        if cv2.waitKey(1) & 0xFF == ord('q'):  # pour avoir une vision en continue
            break  

    print('[INFO] Stopping System')  # mettre un wait de x secondes avant stopping system pour arrêter la picam après
    video_capture.release() 
    cv2.destroyAllWindows()