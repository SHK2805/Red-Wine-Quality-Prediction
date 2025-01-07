from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    # these are the inputs to the data ingestion pipeline
    data_root_dir: Path
    data_source: str
    data_local_data_file: Path
    data_unzip_dir: Path
    data_source_type: str
    data_source_separator: str

@dataclass
class DataValidationConfig:
    # these are the inputs to the data validation pipeline
    data_root_dir: Path
    data_unzip_dir: Path
    STATUS_FILE: str
    all_schema: dict

@dataclass
class DataTransformationConfig:
    # these are the inputs to the data transformation pipeline
    data_root_dir: Path
    data_unzip_dir: Path
    data_preprocessed_file: Path
    data_preprocessed_train_file: Path
    data_preprocessed_test_file: Path
    data_source_train_test_split: float
    data_source_random_state: int

@dataclass
class ModelTrainerConfig:
    # these are the inputs to the model training pipeline
    data_root_dir: Path
    data_train_file: Path
    data_test_file: Path
    model_name: str
    # model parameters
    # We are using ElasticNet model
    # the parameters are alpha and l1_ratio
    # the parameters value are given in params.yaml
    alpha: float
    l1_ratio: float
    target_column: str