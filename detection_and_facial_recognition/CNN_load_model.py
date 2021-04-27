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


class_names=["Alicia","Talla"]
train_path_img = "Test_image/train_img/"
#train_path_img = "Test_image/train_img/Alicia/"
#test_path = "Test_image/test_Talla/Talla/Talla_1.jpeg"
test_path = "Test_image/test_img/Alicia/Alicia_8.jpg"

loaded_model= tf.keras.models.load_model("Access_manager")

img_test = cv2.imread(test_path,cv2.COLOR_BGR2GRAY)
img_test = cv2.resize(img_test,(200,200))


img_test=tf.convert_to_tensor(img_test)
img_test=tf.reshape(img_test, (1,200,200,3))
#test_img= np.expand_dims(img_test,0)
print (img_test.shape)
#test_img=tf.io.decode_image(test_path)
#model.evaluate(train_data,test_img, verbose=1)
result=loaded_model.predict(img_test,verbose=1)
print(class_names[np.argmax(result[0])])

print('Prediction is: ',result)
