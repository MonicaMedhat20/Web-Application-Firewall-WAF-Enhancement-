from aiohttp import get_payload
from flask import Flask, redirect, request, abort, render_template, jsonify, url_for, session
import pickle 
import numpy as np
import tensorflow as tf
from keras.models import load_model
import werkzeug
import re

#creating instance of the app
app = Flask(__name__, static_folder='./static')

model = pickle.load(open('model.pkl', '+rb')) #model generated for dataset1
# model2 = pickle.load(open('model2.pkl', '+rb')) #model generated for dataset2




#loading the pre-trained machine learning model
with open('model.pkl','rb') as model_file:
    RF_model = pickle.load(model_file)

# with open('model2.pkl','rb') as model2_file:
#     RF_model2 = pickle.load(model2_file)

#stacking of two routes to be the same route (leading to the same page) 
@app.route('/')
@app.route('/WAFHome.html/')
def WAFHome():
    return render_template('WAFHome.html')
    

@app.route('/WAFDashboard.html/')
def WAFDashboard():
    return render_template('WAFDashboard.html')


@app.route('/WAFContact.html/')
def WAFContact():
    return render_template('WAFContact.html')


@app.route('/Test.html/')
def Test():
    return render_template('Test.html')

# def analyze_url(url):
#     resu = get_url(url_for)
#     return float(ml_model.predict)

@app.route('/classify', methods = ['POST'])
def classify_handler():
    payload = request.form['payload']
    result =get_payload(payload)  
    class_name = 'Malicious' if result == 1 else 'Normal'
    print('payload:', payload)
    print('result:', result)

    print('class_name:', class_name)

    return {
        'payload' : payload,
        'result' : result,
        'class_name': class_name
    } #return json 




# @app.route('/demo.html/', methods=['GET', 'POST'])
# def demo():
#     if (request.method == 'POST'):
#         payload = request.form.get('payload')
#         return redirect(url_for('home'))
#     return render_template('demo.html')

# @app.route('/demo.html/home.html/')
# def home2():
#     return render_template('home.html')





