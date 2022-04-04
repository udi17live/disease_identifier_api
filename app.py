import string

from flask import Flask, jsonify, request
import os
import pickle
import base64
import io
import random

from tensorflow import keras
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from sklearn.preprocessing import LabelBinarizer
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import numpy as np

import static.helpers as helpers

app = Flask(__name__)

PORT = os.getenv('PORT')
HOST = os.getenv('HOST')


@app.route('/', methods=['GET'])
def index():
    result = {
        'title': 'Pepper Plant Leaf Disease Identification System API',
        'version': 1.0,
        'author': 'Uditha Mahindarathna',
        'github': 'https://github.com/udi17live',
        'description': 'This is an API to detect 2 diseases in the Pepper Plant via Image Processing. That is the Pepper Yellow Mottle Virus and Leaf Blight in pepper. This API is build as a part of my Final Year Project in Level 06 of the B.Eng Software Engineering course from Informatics Institute of Technology Sri Lanka (IIT) affiliated with University of Westminster. The project is purely for Educational Purposes and NOT production ready.'
    }
    return jsonify(result)


@app.route('/predict-disease', methods=['POST'])
def predict_disease():
    payload = request.get_json(force=True)
    encoded_image = payload['image_encoded']

    decoded_image = base64.b64decode(encoded_image)
    leaf_image = Image.open(io.BytesIO(decoded_image))
    image_name_string = string.ascii_letters + string.digits + string.octdigits
    image_name = ''.join((random.choice(image_name_string) for i in range(16))) + '.jpg'
    leaf_image.save(image_name)
    bg_removed_img = helpers.remove_image_background(leaf_image)

    return image_name


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
