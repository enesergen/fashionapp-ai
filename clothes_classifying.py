from keras.models import load_model
from PIL import Image
import numpy as np
from skimage import transform

def load(filename):
   np_image = Image.open(filename)
   np_image = np.array(np_image).astype('float32')/255
   np_image = transform.resize(np_image, (224, 224, 3))
   np_image = np.expand_dims(np_image, axis=0)
   return np_image

class_labels=["CAPS","DRESS","HANDBAG","JACKET"
              ,"PANT","SHIRT","SHOES","SHORT",
              "SKIRT","SUNGLASSES","SWEATERS",
              "SWEATSHIRT","TSHIRT"]



def image_classifying(model,url):
    pred = np.argmax(class_labels, axis=-1)
    image = load(url)
    pred=model.predict(image)
    return class_labels[np.argmax(pred)]

