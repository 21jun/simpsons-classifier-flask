print('importing libraries...')
# Flask
from flask import Flask, request, jsonify
import logging
import random
import time

# Utils
from PIL import Image
import requests
import os
from io import BytesIO
import json
import datetime

# fastai
from fastai import *
from fastai.vision import *
import fastai

# settings
from model import *
from settings import *

print('done!\nsetting up the directories and the model structure...')

print('done!\nlaunching the server...')

app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello World!'


@app.route('/predict', methods=['GET'])
def predict():
    url = request.args['url']
    response = requests.get(url)
    img = open_image(BytesIO(response.content))

    t = time.time()
    pred, _, proba = learn.predict(img)
    dt = time.time() - t
    print(f"Execution time: {dt}")

    print(pred)
    print(proba)
    result = {'predict': str(pred), 'proba':float(proba[proba.argmax()]) ,'date': str(datetime.datetime.now()), "execute time": dt}
    return json.dumps(result)


if __name__ == '__main__':
    # app.run(host = '0.0.0.0', port=8000)
    app.run(port=PORT)
