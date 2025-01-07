import os
from src.e2e_ml_project_1.constants.constants import *
from src.e2e_ml_project_1.entity.config_entity import (DataIngestionConfig,
                                                       DataValidationConfig,
                                                       DataTransformationConfig)
from src.e2e_ml_project_1.logger.logger_config import logger
from src.e2e_ml_project_1.utils.common import read_yaml, create_directories
from src.e2e_ml_project_1.utils.schema_manager import SchemaFileManager


class ConfigurationManager:
    def __init__(self,
                 config_file_path: Path = CONFIG_FILE_PATH,
                 params_file_path: Path = PARAMS_FILE_PATH,
                 schema_file_path: Path = SCHEMA_FILE_PATH):
        self.class_name = self.__class__.__name__
        self.config_file_path: Path = config_file_path
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        # create the artifacts directory
        self.artifacts_dir = self.config.artifacts_root
        logger.info(f"Artifacts directory: {self.artifacts_dir}")
        create_directories([os.path.join(self.artifacts_dir)])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        tag: str = f"{self.class_name}::get_data_ingestion_config::"
        config = self.config.data_ingestion
        logger.info(f"{tag}Data ingestion configuration obtained from the config file")

        # create the data directory
        data_dir = config.data_root_dir
        logger.info(f"{tag}Data directory: {data_dir} obtained from the config file")

        create_directories([data_dir])
        logger.info(f"{tag}Data directory created: {data_dir}")

        data_ingestion_config: DataIngestionConfig = DataIngestionConfig(
            data_root_dir=Path(config.data_root_dir),
            data_source=config.data_source,
            data_local_data_file=Path(config.data_local_data_file),
            data_unzip_dir=Path(config.data_unzip_dir),
            data_source_type=config.data_source_type,
            data_source_separator=config.data_source_separator
        )
        logger.info(f"{tag}Data ingestion configuration created")
        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        tag: str = f"{self.class_name}::get_data_validation_config::"
        config = self.config.data_validation
        logger.info(f"{tag}Data validation configuration obtained from the config file")

        # read schema
        schema = SchemaFileManager(schema=self.schema).get_schema_as_key_value_pairs()
        logger.info(f"{tag}Schema obtained from the schema file")

        # create the data directory
        data_dir = config.data_root_dir
        logger.info(f"{tag}Data directory: {data_dir} obtained from the config file")

        create_directories([data_dir])
        logger.info(f"{tag}Data directory created: {data_dir}")

        data_validation_config: DataValidationConfig = DataValidationConfig(
            data_root_dir=Path(config.data_root_dir),
            data_unzip_dir=Path(config.data_unzip_dir),
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )
        logger.info(f"{tag}Data validation configuration created")
        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        tag: str = f"{self.class_name}::get_data_transformation_config::"
        config = self.config.data_transformation
        logger.info(f"{tag}Data transformation configuration obtained from the config file")

        # create the data directory
        data_dir = config.data_root_dir
        logger.info(f"{tag}Data directory: {data_dir} obtained from the config file")
        create_directories([data_dir])
        logger.info(f"{tag}Data directory created: {data_dir}")

        data_transformation_config: DataTransformationConfig = DataTransformationConfig(
            data_root_dir=Path(config.data_root_dir),
            data_unzip_dir=Path(config.data_unzip_dir),
            data_preprocessed_file=Path(config.data_preprocessed_file),
            data_preprocessed_train_file=Path(config.data_preprocessed_train_file),
            data_preprocessed_test_file=Path(config.data_preprocessed_test_file),
            data_source_train_test_split=config.data_source_train_test_split,
            data_source_random_state=config.data_source_random_state
        )

        return data_transformation_config



