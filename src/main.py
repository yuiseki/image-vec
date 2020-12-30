import io
import json
import base64

from flask import Flask, request, jsonify
import requests
from img2vec_pytorch import Img2Vec
from PIL import Image
import numpy as np

class NumPyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NumPyEncoder, self).default(obj)

app = Flask(__name__)
img2vec = Img2Vec()

@app.route('/')
def root():
    return 'ok'

@app.route('/vector.json', methods=['GET', 'POST'])
def vector():
    if request.method == 'GET':
        url = request.args.get('url')
        res = requests.get(url)
        image = Image.open(io.BytesIO(res.content))
    elif request.method == 'POST':
        image_b64 = request.form['image_b64']
        content = base64.b64decode(image_b64)
        image = Image.open(io.BytesIO(content))
    content_vector = img2vec.get_vec(image)
    return jsonify({
        'content_vector': json.dumps(content_vector, cls=NumPyEncoder)
    })
