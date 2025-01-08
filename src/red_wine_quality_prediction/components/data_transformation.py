import os

import pandas as pd
from sklearn.model_selection import train_test_split

from src.red_wine_quality_prediction.components.data_cleaning import DataCleaning
from src.red_wine_quality_prediction.entity.config_entity import DataTransformationConfig
from src.red_wine_quality_prediction.logger.logger_config import logger


# DataTransformation class
# We can add different data transformation techniques here like scaling, encoding, PCA etc.
# We can also add data cleansing techniques like removing missing values, outliers etc.
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.class_name = self.__class__.__name__
        self.config = config

    def transform_data(self) -> bool:
        tag: str = f"{self.class_name}::transform_data::"
        try:
            # Check if the data is present
            if not os.path.exists(self.config.data_unzip_dir):
                logger.error(f"{tag}Data file {self.config.data_unzip_dir} does not exist")
                return False

            # Read the data
            df = pd.read_csv(self.config.data_unzip_dir)
            logger.info(f"{tag}Data read from: {self.config.data_unzip_dir}")

            # Clean the data
            # Perform EDA and data cleaning
            data = DataCleaning().data_cleaning_pipeline(df)
            logger.info(f"{tag}Data cleaned")

            # Split the data into train and test
            train, test = train_test_split(data,
                                           test_size=self.config.data_source_train_test_split,
                                           random_state=self.config.data_source_random_state)
            logger.info(f"{tag}Data split into train and test with test size: {self.config.data_source_train_test_split}")
            logger.info(f"{tag}Data split into train and test with random state: {self.config.data_source_random_state}")

            # Write the data to the preprocessed files
            data.to_csv(self.config.data_preprocessed_file, index=False)
            logger.info(f"{tag}Data written to preprocessed file: {self.config.data_preprocessed_file}")

            train.to_csv(self.config.data_preprocessed_train_file, index=False)
            logger.info(f"{tag}Train split and written to preprocessed file: {self.config.data_preprocessed_train_file}")

            test.to_csv(self.config.data_preprocessed_test_file, index=False)
            logger.info(f"{tag}Test split and written to preprocessed file: {self.config.data_preprocessed_test_file}")

            logger.info(f"{tag}Data split and written to preprocessed files")

            return True

        except Exception as e:
            logger.error(f"{tag}Error transforming the data: {e}")
            raise e
