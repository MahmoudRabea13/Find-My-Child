from flask import Flask, render_template, request, jsonify, json
import cv2
import numpy as np
from utilities.FaceDetection import FaceDetection
from utilities.Classify import Classify
from utilities.New_PCA import NPCA
app = Flask(__name__)
Face = FaceDetection()
Model = Classify()
pca = NPCA()
Face = FaceDetection()


@app.route('/')
def main():
    Model.load_weights()
    pca.load_preprocessing()
    return render_template('index.html')


@app.route('/input', methods=['POST', 'GET'])
def input():
    if request.method == 'POST':
        img = request.files.get('input_img')
        name = './static/Imgs/' + img.filename + '.jpg'
        img.save(name)
        X_try = cv2.imread('./static/imgs/input_img.jpg', 0)
        n, dim = Face.detect_faces('./static/imgs/input_img.jpg')
        names = ['Rabea', 'Nasser', 'Abdelrhman']
        imgs_n = []
        pred = []
        for i in range(n):
            new_img = X_try[dim[i][1]:dim[i][1]+dim[i]
                            [3], dim[i][0]:dim[i][0]+dim[i][2]]
            new_img = cv2.resize(new_img, (64, 64))
            # cv2.imwrite('./static/Imgs/output_img.jpg',new_img)
            imgs_n.append(new_img)
        imgs_n = np.array(imgs_n)
        ll = pca.preprocess_data(imgs_n)
        ll = pca.reduce_dim(ll)
        for i in range(n):
            y_hat = Model.predict(ll[i, :])
            pred.append(names[y_hat])
        # print(pred)
        # print(n)
        Face.save(pred)
        result = [n, pred]
        # print(result)
        return jsonify(result)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
