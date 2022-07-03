import numpy as np
import keras

from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras.applications.vgg19 import VGG19, preprocess_input, decode_predictions
from keras.models import load_model

model = load_model("/content/model.h5")

def prediction(path):

    img = load_img(path, target_size=(256,256))
    i = img_to_array(img)
    im = preprocess_input(i)
    img = np.expand_dims(im, axis= 0)
    pred = np.argmax(model.predict(img))
    print("pred")

path = "late blight of potato.jpg"

prediction(path)