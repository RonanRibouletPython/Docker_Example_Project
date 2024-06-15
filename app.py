from flask import Flask, request, app, jsonify, url_for, render_template
import pandas as pd
import numpy as np
import pickle
from utilities import windows_to_posix
import flasgger as fl

MODEL_PATH = windows_to_posix(r'Notebooks\linear_regression.pkl')
SCALER_PATH = windows_to_posix(r'Notebooks\scaler.sav')
QUANTILE_PATH = windows_to_posix(r'Notebooks\quantile.sav')

app = Flask(__name__)
fl.Swagger(app)

model_file = open(MODEL_PATH, 'rb')
scaler_file = open(SCALER_PATH, 'rb')
quantile_file = open(QUANTILE_PATH, 'rb')

model = pickle.load(model_file)
scaler = pickle.load(scaler_file)
quantile = pickle.load(quantile_file)

@app.route('/')

def home():
    return 'Hello World'

@app.route('prediction', methods=["GET"])

def prediction_auth_note():
    

@app.route('/prediction', methods=["POST"])
def prediction_api():
    
    data = request.json["data"]
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))

    transformed_data = scaler.transform(quantile.transform(np.array(list(data.values())).reshape(1, -1)))
    
    # Perform the prediction
    prediction = model.predict(transformed_data)
    print(prediction[0])

    return jsonify(str(prediction[0]))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)