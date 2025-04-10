from flask import Flask, request, jsonify
from hybrik_api import analyze_image
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image = Image.open(image_file.stream).convert('RGB')
    image_np = np.array(image)

    result = analyze_image(image_np)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)