import os.path
from pathlib import Path

import pandas as pd
from src.e2e_ml_project_1.entity.config_entity import DataValidationConfig
from src.e2e_ml_project_1.logger.logger_config import logger
from src.e2e_ml_project_1.utils.common import check_file_exists, write_data_to_file


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.class_name = self.__class__.__name__
        self.config = config

    def validate_all_columns(self) -> bool:
        tag: str = f"{self.class_name}::validate_all_columns::"
        validation_status = False
        try:
            # Check if the data is present
            if not check_file_exists(self.config.data_unzip_dir):
                logger.error(f"{tag}Data file {self.config.data_unzip_dir} does not exist")
                logger.info(f"{tag}Writing the validation status {validation_status} to: "
                            f"{self.config.STATUS_FILE}")
                write_data_to_file(Path(os.path.join(self.config.STATUS_FILE)), str(validation_status))
                return validation_status

            # Read the data
            data = pd.read_csv(self.config.data_unzip_dir)
            logger.info(f"{tag}Data read from: {self.config.data_unzip_dir}")
            all_cols = list(data.columns)
            all_schema: dict = self.config.all_schema

            # Check if the data has all the columns
            if set(data.columns) == set(all_schema.keys()):
                logger.info(f"{tag}All columns are present in the data")
                # write to file
                validation_status = True
            else:
                logger.error(f"{tag}Columns in the data do not match the schema")

            logger.info(f"{tag}Writing the validation status {validation_status} to: {self.config.STATUS_FILE}")
            write_data_to_file(Path(os.path.join(self.config.STATUS_FILE)), str(validation_status))
            return validation_status

        except Exception as e:
            logger.error(f"{tag}Error reading the data: {e}")
            logger.info(f"{tag}Writing the validation status {validation_status} to: {self.config.STATUS_FILE}")
            write_data_to_file(Path(os.path.join(self.config.STATUS_FILE)), str(validation_status))
            raise e



