# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 22:06:48 2018

@author: Lenovo
"""

import os
os.chdir("C:\\Users\\Lenovo\\Desktop\\ML\\Neural")

##############################################################################

## Using a pre-trained Object Recognition Model

#loading the image net dataset 
#Load VGG model in keras
#Classifying objects

# VGG - Oxford Visual Geometry Group

#Importing the VGG model

from keras.applications.vgg16 import VGG16
model = VGG16()
model.summary()

plot_model(model, to_file = "vgg.png")

"""
include_top(True)
weights('imagenet')
input_tensor(None)
input_shape(None) #size of the image
polling(None)
classes(1000) #size of output vector
"""

from keras.preprocessing.image import load_img
#loading a image from file
image = img_to_array(image)
# reshape the data according to the model training
image = image.reshape((1,image.shape[0],image.shape[1],image.shape[2]))
from keras.applications.vgg16 import preprocess_input
image = preprocess_input(image)
yhat = model.predict(image)


#Interpret prediction
from keras.applications.vgg16 import decode_predictions
#conver the probabilities to class labels
label = decode_predictions(yhat)
# retrieve the highest probability
label = lable[0][0]
#printing the result
print('%s (%.2f%%)' % ( label[1],label[2]*100))



