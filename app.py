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

@app.route('/Test.php/')
def Test():
    return render_template('Test.php')

@app.route('/Test.php/result.php/')
def forward():
    return render_template('result.php')

@app.route('/result.php/')
def result():
    return render_template('result.php')

@app.route('/result.php/Test.php')
def back():
    return render_template('Test.php')

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
            return jsonify({"result": "Normal"})
        else:
            return jsonify({"result": "Malicious"})
    

if __name__ == "__main__":
    # Save the URLChecker instance
    checker = URLChecker('combined_balanced_urls.csv')  # Update with actual path
    with open('url_checker.pkl', 'wb') as f:
        pickle.dump(checker, f)

    app.run(port=9005)














