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
    data_source_train_test_split: float
    data_source_random_state: int