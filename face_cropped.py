from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop


import PIL
import PIL.Image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import cv2
import os


"""Image classification: process of taking an input (picture) and outputting a class
CNN Process:
- Convolutionnal Layers
- rELu Layers
- Pooling Layers
- A fully connected: connect every neuron in one layer to every neuron in the next layer.

"""

#from tqdm import tqdm


face_cascade = cv2.CascadeClassifier('/Users/tallatoure/Documents/Git/OpenCV/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

#test_img="Alicia_test"
test_path="Test_image/"
#test_var_img = test_path+test_img
#img_test=cv2.imread("Test_image/Alicia_test_img1.jpg")


cv2.resizeWindow('window',600,800)
#print(test_var_img)


#img_test=image.load_img("/Test_image/Alicia_test_img1")
#cv2.imshow('image',img_test)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



### -----Haar Cascade Face detection ---------####


def face_resizing(person_name):

    img_path="Test_image/"
    img_cam_path= img_path+"cam/"+person_name+"/"
    #img_cam_path= img_path+"test_Talla/"

    img_trained_path=img_path+"train_img/"+person_name+"/"

    img_id=14

    while True:

    
        img_name = person_name+"_"+str(img_id)+".jpg"
        img_cam = img_cam_path+img_name
        print(img_cam)

        img_trained = img_trained_path+img_name
        img_cam = cv2.imread(img_cam)


        gray = cv2.cvtColor(img_cam, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)#Face detection

        #print (gray)

    


        for (x,y,w,h) in faces:
            print ("1")
            cv2.rectangle(img_cam,(x,y),(x+w,y+h),(255,0,0),2)
            cropped_face = img_cam[y:y+h,x:x+w]

        #cv2.resize(cropped_face, (200,200))
        cv2.imshow(img_name,cropped_face)
        cv2.imwrite(img_trained,cropped_face)

        if cv2.waitKey(1)==27 or img_id==19:
            break

        img_id=img_id+1

    print("Face Detection done !!")

    cv2.destroyAllWindows()
    return 0
    
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


face_resizing("Alicia")
