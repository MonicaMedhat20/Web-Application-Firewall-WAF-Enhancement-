from aiohttp import get_payload
from flask import Flask, redirect, request, abort, render_template, jsonify, url_for, session
import pickle 
import numpy as np
import tensorflow as tf
from keras.models import load_model
import werkzeug
import re

from Final.main_code import URLChecker, predict_from_url

#creating instance of the app
app = Flask(__name__, static_folder='./static')

# model = pickle.load(open('model.pkl', '+rb')) #model generated for dataset1
# model2 = pickle.load(open('model2.pkl', '+rb')) #model generated for dataset2




#loading the pre-trained machine learning model
# with open('model.pkl','rb') as model_file:
#     RF_model = pickle.load(model_file)

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

# Create Flask application
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """Flask endpoint to predict security risks based on a submitted URL."""
    data = request.json
    url = data.get('url', '')

    # Load the URL checker
    with open('url_checker.pkl', 'rb') as f:
        url_checker = pickle.load(f)

    # Predict security risks
    result = predict_from_url(url)

    if result == 1:
        # If the result is 1, check the URL with URLChecker
        url_check_result = url_checker.check_url(url)
        if url_check_result == 0:
            return jsonify({"result": "Benign"})
        else:
            return jsonify({"result": "Attack"})
    

if __name__ == "__main__":
    # Save the URLChecker instance
    checker = URLChecker('combined_balanced_urls.csv')  # Update with actual path
    with open('url_checker.pkl', 'wb') as f:
        pickle.dump(checker, f)

    app.run(port=9005)







# def analyze_url(url):
#     resu = get_url(url_for)
#     return float(ml_model.predict)

# @app.route('/classify', methods = ['POST'])
# def classify_handler():
#     payload = request.form['payload']
#     result =get_payload(payload)  
#     class_name = 'Malicious' if result == 1 else 'Normal'
#     print('payload:', payload)
#     print('result:', result)

#     print('class_name:', class_name)

#     return {
#         'payload' : payload,
#         'result' : result,
#         'class_name': class_name
#     } #return json 




# @app.route('/demo.html/', methods=['GET', 'POST'])
# def demo():
#     if (request.method == 'POST'):
#         payload = request.form.get('payload')
#         return redirect(url_for('home'))
#     return render_template('demo.html')

# @app.route('/demo.html/home.html/')
# def home2():
#     return render_template('home.html')





