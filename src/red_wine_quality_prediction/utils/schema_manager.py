from pathlib import Path
from typing import Any

from box import ConfigBox
from box.config_box import ConfigBox

from src.red_wine_quality_prediction.constants.constants import SCHEMA_FILE_PATH
from src.red_wine_quality_prediction.logger.logger_config import logger
from src.red_wine_quality_prediction.utils.common import check_file_exists, read_yaml


class SchemaFileManager:
    def __init__(self, schema_file_path: Path = SCHEMA_FILE_PATH, schema: ConfigBox = None):
        self.class_name = self.__class__.__name__
        self.schema_file_path = schema_file_path
        self.schema = schema

    def get_schema_as_config_box(self) -> ConfigBox | None:
        tag: str = f"{self.class_name}::get_schema_as_dict::"
        logger.info(f"{tag}Schema file path: {self.schema_file_path}")
        if not check_file_exists(self.schema_file_path):
            logger.info(f"{tag}Schema file does not exist: {self.schema_file_path}")
            return None
        else:
            logger.info(f"{tag}Schema file exists: {self.schema_file_path}")

        # read the yaml file
        data = read_yaml(self.schema_file_path)
        logger.info(f"{tag}Schema file read successfully")

        return ConfigBox(data)

    def get_schema_as_dict(self) -> dict[str, dict[Any, Any]]:
        tag: str = f"{self.class_name}::get_schema_as_dict::"
        if self.schema is None:
            self.schema = self.get_schema_as_config_box()
        # get the first key from the schema
        data = self.schema
        first_key = list(data.keys())[0]

        # get values for the first key
        first_key_values = data[first_key]

        # the values for the first_key_values are in the format of [{'name': 'fixed acidity', 'type': 'float64'}, ...]
        # get all the values for the 'name' key
        names = [value['name'] for value in first_key_values]

        # get all the values for the 'type' key
        types = [value['type'] for value in first_key_values]

        # get the values for the 'TARGET_COLUMN' key
        target_column_values = data['TARGET_COLUMN']

        # get all the values for the 'name' key in the 'TARGET_COLUMN' key
        target_column_names = [value['name'] for value in target_column_values]

        # get all the values for the 'type' key in the 'TARGET_COLUMN' key
        target_column_types = [value['type'] for value in target_column_values]

        # create a dictionary with the names and types of the columns
        columns_dict = dict(zip(names, types))

        # create a dictionary with the names and types of the target columns
        target_columns_dict = dict(zip(target_column_names, target_column_types))
        logger.info(f"{tag}completed")
        return {"columns": columns_dict, "target_columns": target_columns_dict}


    def get_schema_as_key_value_pairs(self) -> dict:
        tag: str = f"{self.class_name}::get_schema_as_key_value_pairs::"
        schema = self.get_schema_as_dict()
        key_value_pairs = {}
        for dictionary in schema.values():
            key_value_pairs.update(dictionary)

        logger.info(f"{tag}completed")

        return key_value_pairs

    def get_schema_file_path(self) -> Path:
        return self.schema_file_path

    def set_schema_file_path(self, schema_file_path: Path) -> None:
        self.schema_file_path = schema_file_path
        logger.info(f"Schema file path has been set to: {schema_file_path}")