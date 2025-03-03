# Machine Learning project
* This is a template for a Machine Learning project.

### Dataset
* The dataset description is given in the **data_description.md** file

### Technologies
* The project is built using the following technologies:
  * Python
  * Flask
  * MLFlow
  * ElasticNet
  * Pandas
  * Numpy
  * Scikit-learn

### Steps
#### MLFlow
* Before running the model evaluation pipeline or the model prediction pipeline make sure the **mlflow server is running**
* Make sure the correct **mlflow uri** is set in the config file **config.yaml**
* Add **mlflow** package to the **requirements.txt** file or install it manually using `pip install mlflow`
  * The other packages needed are given in the **requirements.txt** file
* Make sure the mlflow server port does not conflict with any other port on your machine
* Make sure the mlflow server port does not conflict with Flask server port on your machine
* * Run the mlflow server using the following command
* Open the terminal and run the following command
```bash
# mlflow server will be running on localhost: 127.0.0.1 and on port: 8080
mlflow server --host 127.0.0.1 --port 8080
```
* Access the mlflow server at http://127.0.0.1:8080/ 
* Run the MLFlow and Flask in two different terminals

#### Flask
* Before running the Flask API make sure the **Flask server is running**, to run the flask server flollow the below steps
* Make sure the correct **Flask server host ip** and  **Flask server port** is set in the app.py file
```python
# Flask server will be running on localhost:127.0.0.1  and on port: 5000
from flask import Flask
app = Flask(__name__) 
app.run(host="0.0.0.0", port=5000)
```
* Open the terminal and run the following command
```bash
python app.py
```
* Access the flask app at http://127.0.0.1:5000

#### Run
* To run the ML pipeline run the following steps
* Open the flask app at http://127.0.0.1:5000
* Train the model using the train page http://127.0.0.1:5000/train
  * This will trigger the model training and evaluation pipeline from main.py
* Go to the home page to give input values for the model at http://127.0.0.1:5000
* Click on the **predict** button to get the prediction. This will navigate to the result page http://127.0.0.1:5000/result

#### Clean
* To delete the artifacts, logs and mlflow folders run the code in **clean.py**

### Explanation
* The project is a template for a Machine Learning project.
* The implementation is done in the **components** package
* The data ingestion pipeline downloads the zipfile and extracts the csv
  * Data file extracted to: artifacts\data_ingestion
* The data validation pipeline validates the data features using the schema.yaml file 
  * Writs the status to artifacts/data_validation/status.txt
* The data transformation pipeline performs the data cleaning and feature engineering. 
  * Performs the train test split and saves the train and test data into csv files
  * The train and test data is saved to 
    * artifacts\data_transformation\train.csv
    * artifacts\data_transformation\test.csv
* The model training pipeline gets the train and test data from csv, trains the model using the train data and saves the model in the artifacts folder
  * Data read from: artifacts\data_transformation\train.csv and artifacts\data_transformation\test.csv
  * the model is saved to: artifacts\model_trainer\model.joblib
* The model evaluation pipeline evaluates the model using the test data it gets from the csv and saves the metrics in the artifacts folder ad mlflow
  *  Metrics data saved to the JSON file: artifacts\model_evaluation\metrics.json

### ML Pipeline
* The ML pipeline is a sequence of steps that are executed in order to build, train, evaluate, and deploy a machine learning model.
* Below are the steps in the ML pipeline:
1. Data Collection
2. Data Ingestion
3. Data Transformation
4. Model Training
5. Model Evaluation (using MLFlow)
6. Model Deployment
7. Model Monitoring
8. Model Retraining

### Workflow
* We update the below files in that order to achieve the ML pipeline:
1. config > config.yaml
   1. data_ingestion
   2. data_validation
   3. data_transformation
   4. model_training
2. schema.yaml
   1. The schema of the data i.e. the column headers and the data types
   2. data_validation
3. params.yaml
   1. The hyperparameters for the model
   2. model_training
4. Update the entity
   1. In src > entity > config_entity.py
5. Update the configuration manager 
   1. In src > config > configuration.py
6. Update the components 
   1. In src > components 
      1. data_ingestion.py
      2. data_validation.py
      3. data_transformation.py
      4. model_trainer.py
      5. model_evaluation.py
7. Update the pipeline
    1. In src > pipeline
        1. data_ingestion.py
        2. data_validation.py
        3. data_transformation.py 
        4. model_trainer.py
        5. model_evaluation.py
        6. prediction.py
           1. The prediction pipeline is written only in this file the other above steps are not used in the prediction pipeline
8. Update the main.py
    1. In main.py
9. Predictions
   1. Create the templates folder with the html files
   2. Create the app.py for the Flask API
      1. The app.py file is the main file where we run the Flask API
   3. The index.html file is the main file where we give the input to the model and get the output into the result.html file
   4. There is function /predict  that is index.html that is defined in the app.py file 
   5. The result.html file is the file where we get the output of the model
   6. Follow the below steps to run the app
      1. open the terminal and run the following command
      2. python app.py
      3. The app will run on the localhost http://127.0.0.1/ and port 8080 of the local machine
      4. To access the app go to the http://127.0.0.1:5000
      5. to train the model go to the train page http://127.0.0.1:5000/train
      6. give the values to the form and click on the predict button to get the prediction