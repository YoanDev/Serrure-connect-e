# Source Code - Defend Intelligence
import cv2
import socket
import numpy as np
import face_recognition
import os
import ntpath
import random
import time
from os import listdir
from os.path import isfile, join
import sys
import shutil
import datetime

class reco:
    def __init__(self):
        pass
    
    def easy_face_reco(self,frame, known_face_encodings, known_face_names):  # fait la comparaison des visages stockés en BD et ceux récupérés en entrée
        count = 0
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
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)

                 # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                     first_match_index = matches.index(True)
                     name = known_face_names[first_match_index]
                     return "open"
                else:
                    count += 1          
                    
            if len(face_encodings) != 0:   
                if count == len(face_encodings):
                    cv2.imwrite("new_faces/test.png", frame)
                    name = "Unknown_visage"  # partie interaction avec le propriétaire à rajouter et ouverture ou non de la sérrure
                    return "Ne sait pas"
            else:
                return "Aucun visage"
                

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

    def intro(self):
        
        # Define the duration (in seconds) of the video capture here
        capture_duration = 10
    
        print('[INFO] Importing faces...')
        face_to_encode_path = [f for f in listdir("known_faces") if isfile(join("known_faces", f))]
        
        if len(face_to_encode_path)==0:
            raise ValueError('No faces detect in the directory: {}'.format(face_to_encode_path))
        
        known_face_names = face_to_encode_path#  on charge dans un tab l'ensemble des noms des différentes images en BD ouvert sous forme de files
        known_face_encodings = []
        
        for file_ in face_to_encode_path:
            image = face_recognition.load_image_file("known_faces/"+file_)
            try:
                face_encoded = face_recognition.face_encodings(image)[0]
            except IndexError as e:
                print(e)
                pass
                #sys.exit(1)
            known_face_encodings.append(face_encoded)   #  on charge dans un tab l'ensemble des visages de la BD encodés
        print('[INFO] Faces well imported')
        print('[INFO] Starting Webcam...') # qui sera déclenché pour notre cas par le OK du capteur infrarouge (webcam = picam pour nous) 
        video_capture = cv2.VideoCapture(0)
        #changer la taille de la video ici avec video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
        print('[INFO] Start detecting...') 
        start_time = time.time()
        while( int(time.time() - start_time) < capture_duration ):
            ret, frame = video_capture.read()
            rec = self.easy_face_reco(frame, known_face_encodings, known_face_names)
            if rec == "open":
                video_capture.release() 
                cv2.destroyAllWindows()
                return "open"
            cv2.imshow('Easy Facial Recognition App', frame) # to display an image in a window

            if cv2.waitKey(1) & 0xFF == ord('q'):  # pour avoir une vision en continue
                break  

        print('[INFO] Stopping System')  # mettre un wait de x secondes avant stopping system pour arrêter la picam après
        video_capture.release() 
        cv2.destroyAllWindows()
        if rec == "Ne sait pas":
            return "Ne sait pas"
        else:
            return "Aucun visage"
    
    def copy_new_photo(self):
        date = datetime.datetime.now()
        shutil.copy('new_faces/test.png','known_faces/')
        os.rename('known_faces/test.png','known_faces/'+date.strftime('%s'))
        os.remove('new_faces/test.png')


    
