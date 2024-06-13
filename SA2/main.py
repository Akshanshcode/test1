import numpy as np
import os
import cv2
from cvzone.FaceDetectionModule import FaceDetector

path = "Face-image-dataset-small"
ages=[]
detector = FaceDetector()
img=[]
for img in os.listdir(path):
    try:
        print(img)

        # Check if img is not equal to .git i.e a wrong format image 
        if img!='.git':
            # Get the age from the image path i.e img
            age = img.split("_")[0]
            #Append age to ages array
            genders = img.split("_")[1]
            # Read the image
            img = cv2.imread(str(path)+"/"+str(img))
            # Convert image from BGR to RGB format
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

            # Display the age on the image
            ages.append(age)
    except:
        print("error in reading")

# Convert ages to np.array
ages = np.array(ages,dtype=np.int64)
# Print ages
print ("ages",ages)