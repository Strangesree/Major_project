from flask import Flask, render_template,request,flash,redirect,url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image, ImageOps 
import os
from app_2 import model_predict
from collections import Counter

app = Flask(__name__)

model = load_model('models/LSTM.h5')

categories = ['Normal', 'Overload', 'Underload']

@app.route('/',methods=['POST','GET'])
def recv():
    if request.method == 'POST':
        easy_file = request.files['easy_file']  
        if easy_file:
            easy_file.save('static/uploads/' + easy_file.filename)
            easy_file_path = 'static/uploads/' + easy_file.filename
            predictions, file_name = model_predict(easy_file_path, model)
            frequency = Counter(predictions)
            level = frequency.most_common(1)[0][0]
            result = categories[level]
            # print("The most frequent element is:", level)
            # print("output:", categories[level])
            return render_template('index2.html', result=result, file_name=file_name)
    return render_template('index.html')

@app.route('/reverse_reading')
def reverse_reading():
    return render_template('reverse_reading.html')

@app.route('/numerical_pyramid')
def numerical_pyramid():
    return render_template('numerical_pyramid.html')

@app.route('/spot_the_difference')
def spot_the_difference():
    return render_template('spot_the_difference.html')

@app.route('/find_the_number')
def find_the_number():
    return render_template('find_the_number.html')

@app.route('/stroop_test')
def stroop_test():
    return render_template('stroop_test.html')

@app.route('/ml_analyse')
def ml_analyse():
    return render_template('index2.html')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')