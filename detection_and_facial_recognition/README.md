# Easy Facial Recognition

Recognition by minimum norm between vectors (128D dlib descriptor)
![Alt Text](readme.gif)


## Prerequisites

Make sure to have the following libraries installed in your Python environment:

- opencv
- dlib
- numpy
- imutils
- pillow

Update the known_faces directory with images of people you want to detect (be sure to crop around the faces as the Zuckerberg, Emmmanuel Macron, me and Sammuel Etoo examples.).

Please only use .jpg or .png files.


Unzip le fichier model_preentraine.zip dans le dossier model_preentraine pour avoir les modèles pré-entraînés

## Run

```
python detection_and_facial_recognition.py --i known_faces
```

## TEST method: CNN recognition 

The CNN recognition scripts are running on an environment test on UNIX/Mac0S Big Sur and python 3.6.7. The following libraries are needed: 
- opencv
- tensorflow

These 2 paths have to be created from the location of the current scripts: 
- /Test_image/train_image : Put folders with the pictures of the autrhorized users (one folder per user)
- /Test_image/test_img :  Put the test pictures of users 

```
python3 CNN_face_reco.py 
```
