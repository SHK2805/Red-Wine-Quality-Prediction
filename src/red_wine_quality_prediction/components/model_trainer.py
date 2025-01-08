import os
import joblib
import pandas as pd
from sklearn.linear_model import ElasticNet
from src.red_wine_quality_prediction.entity.config_entity import ModelTrainerConfig
from src.red_wine_quality_prediction.logger.logger_config import logger


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.class_name = self.__class__.__name__
        self.config = config

    def train_model(self):
        tag: str = f"{self.class_name}::train_model::"
        try:
            # Read the data
            train_data = pd.read_csv(self.config.data_train_file)
            test_data = pd.read_csv(self.config.data_test_file)
            logger.info(f"{tag}Data read from: {self.config.data_train_file} and {self.config.data_test_file}")

            # Get the features and target
            X_train = train_data.drop(columns=[self.config.target_column], axis=1)
            y_train = train_data[self.config.target_column]

            X_test = test_data.drop(columns=[self.config.target_column], axis=1)
            y_test = test_data[self.config.target_column]
            logger.info(f"{tag}Features and target obtained")

            # Create the model
            random_state = 42
            model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=random_state)
            model.fit(X_train, y_train)
            logger.info(f"{tag}Model trained with\n"
                        f"alpha: {self.config.alpha}\n"
                        f"l1_ratio: {self.config.l1_ratio}\n"
                        f"random state: {random_state}")

            # Save the model
            model_path = os.path.join(self.config.data_root_dir, f"{self.config.model_name}")
            logger.info(f"{tag}Saving the model to: {model_path}")
            joblib.dump(model, model_path)
            logger.info(f"{tag}Model saved to: {model_path}")

        except Exception as e:
            logger.error(f"{tag}Error training the model: {e}")
            raise e