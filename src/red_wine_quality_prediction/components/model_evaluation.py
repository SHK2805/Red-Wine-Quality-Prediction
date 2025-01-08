from urllib.parse import urlparse

import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from mlflow.models import infer_signature
from sklearn.metrics import (classification_report,
                             confusion_matrix,
                             mean_squared_error,
                             mean_absolute_error,
                             r2_score)

from src.red_wine_quality_prediction.entity.config_entity import ModelEvaluationConfig
from src.red_wine_quality_prediction.logger.logger_config import logger
from src.red_wine_quality_prediction.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.class_name = self.__class__.__name__
        self.config = config

    def evaluate_metrics(self, actual, predicted):
        tag: str = f"{self.class_name}::evaluate_metrics::"
        try:
            logger.info(f"{tag}Evaluating metrics for problem type: {self.config.problem_type}")
            if self.config.problem_type == "classification":
                # Classification metrics
                cm = confusion_matrix(actual, predicted)
                cr = classification_report(actual, predicted)
                return cm, cr
            elif self.config.problem_type == "regression":
                # Regression metrics
                mse = mean_squared_error(actual, predicted)
                mae = mean_absolute_error(actual, predicted)
                r2 = r2_score(actual, predicted)
                return mse, mae, r2
            else:
                message: str = f"{tag}Invalid problem type: {self.config.problem_type}"
                logger.error(message)
                raise Exception(message)
        except Exception as e:
            logger.info(f"{tag}Error evaluating metrics: {e}")
            raise e

    def log_into_mlflow(self):
        tag: str = f"{self.class_name}::log_into_mlflow::"
        try:
            model = joblib.load(self.config.model_path)
            test_data = pd.read_csv(self.config.data_test_file)
            # split the data into X and y
            X_test = test_data.drop(self.config.target_column, axis=1)
            y_test = test_data[self.config.target_column]

            # mlflow logging
            mlflow.set_tracking_uri(self.config.mlflow_uri)
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            with mlflow.start_run():
                predicted = model.predict(X_test)

                if self.config.problem_type == "classification":
                    cm, cr = self.evaluate_metrics(y_test, predicted)
                    logger.info(f"{tag}Confusion Matrix: {cm}")
                    logger.info(f"{tag}Classification Report: {cr}")
                    mlflow.log_metric("Confusion Matrix", cm)
                    mlflow.log_metric("Classification Report", cr)
                    # save the metrics as JSON
                    metrics = {
                        "confusion_matrix": cm.tolist(),
                        "classification_report": cr
                    }
                    save_json(self.config.metrics_file_name, metrics)

                elif self.config.problem_type == "regression":
                    mse, mae, r2 = self.evaluate_metrics(y_test, predicted)
                    logger.info(f"{tag}Mean Squared Error: {mse}")
                    logger.info(f"{tag}Mean Absolute Error: {mae}")
                    logger.info(f"{tag}R2 Score: {r2}")
                    mlflow.log_metric("Mean Squared Error", mse)
                    mlflow.log_metric("Mean Absolute Error", mae)
                    mlflow.log_metric("R2 Score", r2)
                    # save the metrics as JSON
                    metrics = {
                        "mean_squared_error": mse,
                        "mean_absolute_error": mae,
                        "r2_score": r2
                    }
                    save_json(self.config.metrics_file_name, metrics)
                else:
                    message: str = f"{tag}Invalid problem type: {self.config.problem_type}"
                    logger.error(message)
                    raise Exception(message)

                # log the model parameters
                mlflow.log_params(self.config.all_params)

                # log the model for a type file and uri
                if tracking_url_type_store != "file":
                    mlflow.sklearn.log_model(model,
                                             "model",
                                             signature=infer_signature(X_test, predicted),
                                             registered_model_name="ElasticNet")
                    logger.info(f"{tag}Model has been logged into mlflow")
                else:
                    mlflow.sklearn.log_model(model, "model")
                    logger.info(f"{tag}Model has been logged into mlflow")
        except Exception as e:
            logger.info(f"{tag}Error logging into mlflow: {e}")
            raise e
