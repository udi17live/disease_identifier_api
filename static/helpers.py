import base64
import os
import pickle
import requests
import io
import string
import random

from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.image import img_to_array


# Remove Background from Image
def remove_image_background(image):
    api_url = os.getenv('REMOVEBG_API_URL')
    api_key = os.getenv('REMOVEBG_API_KEY')

    resp = requests.post(
        api_url,
        files={'image_file': open(image, 'rb')},
        data={'size': 'auto', 'bg_color': '#d0d0d0'},
        headers={'X-Api-Key': api_key}
    )

    if resp.status_code == requests.codes.ok:
        with open(image, 'wb') as out:
            out.write(resp.content)
            return out
    else:
        print("Error:", resp.status_code, resp.text)
        return False


def get_cnn_model_and_labels():
    label_file_name = 'static/models_labels/labels_pepperleaf_v_{}.pkl'.format(os.getenv('MODEL_VERSION'))
    model_file_name = 'static/models_labels/model_pepperleaf_v_{}.model'.format(os.getenv('MODEL_VERSION'))

    model = load_model(model_file_name)
    labels = pickle.load(open(label_file_name, 'rb'))
    n_classes = labels.classes_
    models_labels = {
        'model': model,
        'n_classes': n_classes
    }

    return models_labels


def pre_process_images(img, target_size):
    if img.mode is not "RGB":
        img = img.convert('RGB')

    img = img.resize(target_size)
    img = img_to_array(img)
    img = img / 255.0
    img = img.reshape(1, 256, 256, 3)

    return img
