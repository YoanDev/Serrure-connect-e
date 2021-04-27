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


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
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

    img_id=1

    while True:

        
    
        img_name = person_name+"_"+str(img_id)+".jpg"
        img_cam = img_cam_path+img_name

        img_trained=img_trained_path+img_name
    
        img_cam=cv2.imread(img_cam)

        gray= cv2.cvtColor(img_cam, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) #Face detection 

        for (x,y,w,h) in faces:
            cv2.rectangle(img_cam,(x,y),(x+w,y+h),(255,0,0),2)
            cropped_face= img_cam[y:y+h,x:x+w]

        cv2.resize(cropped_face, (200,200))
        cv2.imshow(img_name,cropped_face)
        cv2.imwrite(img_trained,cropped_face)

        if cv2.waitKey(1)==13 or img_id==32:
            break

        img_id=img_id+1

    print("Face Detection done !!")

    cv2.destroyAllWindows()
    return 0
    
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

face_resizing("Yoan")
#train_img=ImageDataGenerator(rescale=1/255)
#valid_img=ImageDataGenerator(rescale=1/255)
#train_data= train.flow_from_directory('train',size=(200,200)
#plt.imshow(img_test)
#plt.show()


#3 layers networks




class_names = ['Alicia',"Other"]
#class_names = [0]

#normalization_layer = layers.experimental.preprocessing.Rescaling(1./255)


train_path_img = "Test_image/train_img/"
#train_path_img = "Test_image/train_img/Alicia/"
#test_path = "Test_image/test_Talla/Talla/Talla_1.jpeg"
test_path = "Test_image/test_img/Alicia/Alicia_8.jpg"

#data_dir = pathlib.Path(train_path_img)

#train_dir_img= os.path.join(train_path_img, 'train')
#test_dir_img= os.path.join(test_path, 'test')

BATCH_SIZE=32
IMG_SIZE=(200,200)

train_data = tf.keras.preprocessing.image_dataset_from_directory(train_path_img,
                                             shuffle=True,
                                             validation_split=0.3,
                                             subset="training",
                                             seed=123,
                                             batch_size=BATCH_SIZE,
                                             image_size=IMG_SIZE)

validation_data = tf.keras.preprocessing.image_dataset_from_directory(train_path_img,
                                             validation_split=0.3,
                                             shuffle=True,
                                             subset="validation",
                                             seed=123,
                                             batch_size=BATCH_SIZE,
                                             image_size=IMG_SIZE)

num_classes = 1
"""
#x_train = x_train.reshape(60000, 784).astype("float32") / 255
#x_test = x_test.reshape(10000, 784).astype("float32") / 255

#Alicia_array=np.array(["Alicia"],["Alicia","Alicia","Alicia","Alicia","Alicia","Alicia","Alicia","Alicia"])
Alicia_data=[]
for  i in range (1,10,1):
    Alicia_data.append(1)

Alicia_array=np.array([Alicia_data])

def create_data():
    
    data=[]
    for  i in range (1,10,1):
        img = train_path_img + "Alicia_"+str(i)+".jpg"
        print(img)
        img = cv2.imread(img)
        img_data= cv2.resize(img,(200,200))
        data.append([np.array(img)])

    return data


"""
class_names=train_data.class_names
print(train_data)
#print(train_data[2])
print(validation_data)
print(class_names)

"""
train_data= np.array(create_data())
train_data = train_data/255.0
train_dataset = tf.data.Dataset.from_tensor_slices(train_data)
train_dataset = tf.data.Dataset.from_tensor_slices(ALicia_array)
"""
#print(len(train_data))


# array [[img],[1,0]]
# array [[img],[0,1]]

def generate_cnn_model():

    
    #32 filters
    #relu actiavation g(z)=max(0,z);
    
    model = tf.keras.Sequential([


    #tf.keras.layers.experimental.preprocessing.Rescaling(1./255),
    
    

    tf.keras.layers.Conv2D(32,(3,3),activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=2, strides=2),

    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=2, strides=2),

    #tf.keras.layers.Conv2D(32,(3,3),activation='relu'),
    #tf.keras.layers.MaxPool2D(pool_size=2, strides=2),

    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=2, strides=2),

    tf.keras.layers.Conv2D(128,(3,3),activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=2, strides=2),
    
    #tf.keras.layers.Conv2D(512,(3,3),activation='relu'),
    #tf.keras.layers.MaxPool2D(pool_size=2, strides=2),

    #tf.keras.layers.Conv2D(128,(3,3),activation='relu'),
    #tf.keras.layers.MaxPool2D(pool_size=2, strides=2),


    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1024,activation="relu"),
    tf.keras.layers.Dense(2,activation='softmax'),

    ])

    return model



model= generate_cnn_model()
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


#history = model.fit(train_img_path, class_names, n_epoch=12, validation_data= validation_data, show_metric = True, run_id="FRS" )
history = model.fit(train_data,validation_data=validation_data,epochs=15)
tf.saved_model.save(model,"Access_manager/")

#history = model.fit(train_path_img, class_names, epochs=12, show_metric = True, run_id="FRS" )
#test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

model.summary()


#img_test = image.load_img(test_path, target_size=(200, 200))

img_test = cv2.imread(test_path,cv2.COLOR_BGR2GRAY)
img_test = cv2.resize(img_test,(200,200))
#test_img = np.array(img_test)

#img_test = image.load_img(test_path, target_size=(200, 200))
#img_test_array = image.img_to_array(img_test)
#test_img= np.expand_dims(img_test,0)
#print (test_img)
"""test_img= tf.keras.preprocessing.image_dataset_from_directory(test_path,
                                                                shuffle=True,
                                                                subset="validation",
                                                                validation_split=0.9,
                                                                seed =123,
                                                                batch_size=BATCH_SIZE,
                                                                image_size=IMG_SIZE)
"""


img_test=tf.convert_to_tensor(img_test)
img_test=tf.reshape(img_test, (1,200,200,3))
#test_img= np.expand_dims(img_test,0)
print (img_test.shape)
#test_img=tf.io.decode_image(test_path)
#model.evaluate(train_data,test_img, verbose=1)
result=model.predict(img_test,verbose=1)
print(class_names[np.argmax(result[0])])

print('Prediction is: ',result)



#cv2.rectangle(frame,(rect[0],rect[1]),(rect[2],rect[3]),(255,0,0))
#face_resizing("Alicia")
#face_resizing("Talla")
face_resizing("Yoan")


