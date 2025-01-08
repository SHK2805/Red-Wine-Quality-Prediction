import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.class_name: str = self.__class__.__name__
        self.model_dir = Path("artifacts/model_trainer")
        self.model_file_path = f"{self.model_dir}/model.joblib"
        self.model = joblib.load(self.model_file_path)

    def get_model_file_path(self):
        return self.model_file_path

    def predict(self, input_data: np.array) -> np.array:
        """
        Predict the class label for the input data
        :param input_data:  for prediction
        :return: Predicted class label
        """

        # Make predictions using the loaded model
        # the data should already be reshaped when passing to this method
        predictions = self.model.predict(input_data)

        return predictions