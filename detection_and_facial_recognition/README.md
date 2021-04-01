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

