# flask application to use the prediction model
from src.e2e_ml_project_1.pipeline.prediction import PredictionPipeline
from flask import Flask, request, jsonify, render_template
import os
import numpy as np
import pandas as pd

# to run the app
# open the terminal and run the following command
# python app.py
# to train the model go to the train page http://127.0.0.1:8080/train
# give the values to the form and click on the predict button to get the prediction
app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
def home():
    return render_template("index.html")


@app.route('/train', methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!"


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            # number of input features should be equal to the number of input features in the model
            # here there are 11 input features
            # get the data from the form
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            # put data in a list
            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide,
                    total_sulfur_dioxide, density, pH, sulphates, alcohol]
            # reshaping the data to match the model input
            # because we have 11 input features so we need to reshape the data to 1,11
            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction=str(predict))

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    # the app will run on the localhost http://127.0.0.1/ and port 5000 of the local machine
    # url: http://127.0.0.1:5000/
    app.run(host="0.0.0.0", port=5000)
