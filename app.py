from flask import Flask, jsonify, request
import os

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


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
