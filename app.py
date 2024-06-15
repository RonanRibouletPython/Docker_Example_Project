from flask import Flask, request, app, render_template
import pandas as pd
import numpy as np
import pickle
from utilities import windows_to_posix
import flasgger as fl

MODEL_PATH = windows_to_posix(r'linear_regression.pkl')
SCALER_PATH = windows_to_posix(r'scaler.sav')
QUANTILE_PATH = windows_to_posix(r'quantile.sav')

app = Flask(__name__)

model_file = open(MODEL_PATH, 'rb')
scaler_file = open(SCALER_PATH, 'rb')
quantile_file = open(QUANTILE_PATH, 'rb')

model = pickle.load(model_file)
scaler = pickle.load(scaler_file)
quantile = pickle.load(quantile_file)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''

    '''

    data = [float(x) for x in request.form.values()]
    final_input = scaler.transform(quantile.transform(np.array(data).reshape(1, -1)))

    prediction = model.predict(final_input)[0]

    return render_template('home.html', prediction_text='The predicted authentication bank note: {}'.format(prediction))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)