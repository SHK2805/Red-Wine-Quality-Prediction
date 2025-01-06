import os.path
import pandas as pd
import urllib.request as request
import zipfile
from src.e2e_ml_project_1.entity.config_entity import DataIngestionConfig, DataValidationConfig
from src.e2e_ml_project_1.logger.logger_config import logger
from src.e2e_ml_project_1.utils.common import create_directories, check_file_exists


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.class_name = self
        self.config = config

    def validate_all_columns(self) -> bool:
        tag: str = f"{self.class_name}::validate_all_columns::"
        try:
            validation_status = None
            # Check if the data is present
            if not check_file_exists(self.config.data_root_dir):
                logger.error(f"{tag}Data file does not exist")
                return False

            # Read the data
            data = pd.read_csv(self.config.data_root_dir)
            logger.info(f"{tag}Data read from: {self.config.data_root_dir}")
            all_cols = list(data.columns)
            all_schema: dict = self.config.all_schema

            # Check if the data has all the columns
            if set(data.columns) == set(all_schema.keys()):
                logger.info(f"{tag}All columns are present in the data")
                return True
            else:
                logger.error(f"{tag}Columns in the data do not match the schema")
                return False
        except Exception as e:
            logger.error(f"{tag}Error reading the data: {e}")
            return False


