from aiohttp import get_payload
from flask import Flask, redirect, request, abort, render_template, jsonify, url_for, session
import pickle 
import numpy as np
import tensorflow as tf
from keras.models import load_model
import werkzeug
import re

#creating instance of the app
app = Flask(__name__)

model = pickle.load(open('model.pkl', '+rb')) #model generated for dataset1
model2 = pickle.load(open('model2.pkl', '+rb')) #model generated for dataset2




#loading the pre-trained machine learning model
with open('model.pkl','rb') as model_file:
    RF_model = pickle.load(model_file)

with open('model2.pkl','rb') as model2_file:
    RF_model2 = pickle.load(model2_file)

#stacking of two routes to be the same route (leading to the same page) 
@app.route('/')
@app.route('/WAFHome.html')
def home():
    return render_template('WAFHome.html')
  
def classifyRequest(payload):
    resu = get_payload(payload)
    return float(model2.predict)

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

@app.route('/demo.html/', methods=['GET', 'POST'])
def demo():
    if (request.method == 'POST'):
        payload = request.form.get('payload')
        return redirect(url_for('home'))
    return render_template('demo.html')

@app.route('/demo.html/home.html/')
def home2():
    return render_template('home.html')





# Basic WAF function
def waf(request):
    # SQL injection prevention
    for value in request.values.values():
        if any(keyword in value for keyword in ["SELECT", "INSERT", "UPDATE", "DELETE", "FROM", "WHERE"]):
            abort(403)
    # Cross-Site Scripting (XSS) prevention
    for value in request.values.values():
        if "<script>" in value:
            abort(403)
    return None

@app.route('/request')
def index():
    waf(request)
# Define a simple feature extraction function (replace with your actual feature extraction logic)
def extract_features(payload):
    # Example: Just count the number of characters in the request
    return [[len(payload)]]

# Route to handle form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        request_data = request.form['request_data']
        # Extract features using your feature extraction function
        features = extract_features(request_data)
        # Make a prediction using the pre-trained model
        prediction = model.predict(features)
        prediction = model2.predict(features)
        # Display the result on the web page
        result = 'Malicious' if prediction[1] == 0 else 'Normal'
        return render_template('home.html', request_data=request_data, result=result)


if __name__ == "__main__":
    app.run(debug=True, port= 5000)



# # Your WAF logic goes here
# def check_url(url):
#     # Placeholder logic - replace this with your actual WAF logic
#     if "example.com" in url:
#         return {"message": "URL is allowed"}
#     else:
#         return {"message": "URL is blocked"}

# @app.route("/")
# def index():
#     return app.send_static_file("home.html")

# @app.route("/check_url", methods=["POST"])
# def check_url_route():
#     data = request.json
#     url = data.get("url")
#     if url:
#         result = check_url(url)
#         return jsonify(result)
#     else:
#         return jsonify({"message": "Invalid request"}), 400
    
