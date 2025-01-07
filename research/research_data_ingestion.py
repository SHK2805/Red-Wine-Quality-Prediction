import os.path
import zipfile
from dataclasses import dataclass
from src.e2e_ml_project_1.constants.constants import *
from src.e2e_ml_project_1.utils.common import read_yaml, create_directories
import urllib.request as request
from src.e2e_ml_project_1.logger.logger_config import logger


@dataclass
class DataIngestionConfig:
    data_root_dir: Path
    data_source: str
    data_local_data_file: Path
    data_unzip_dir: Path
    data_source_type: str
    data_source_separator: str


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

# Data Ingestion
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.class_name = self.__class__.__name__
        self.config = config

    # downloading the file
    def download_file(self):
        tag: str = f"{self.class_name}::download_file::"
        # check if the file exists
        if not os.path.exists(self.config.data_local_data_file):
            filename, headers = request.urlretrieve(self.config.data_source, self.config.data_local_data_file)
            logger.info(f"{tag}Source: {self.config.data_source}\nFile downloaded: {filename}\nHeaders: {headers}\nDestination: {self.config.data_local_data_file}")
        else:
            logger.info(f"{tag}File already exists: {self.config.data_local_data_file}")

    # extracting the file
    def extract_file(self):
        tag: str = f"{self.class_name}::extract_file::"
        # check if the file is a ZIP file
        if self.config.data_local_data_file.suffix == ".zip":
            # create the directory to extract the file
            create_directories([self.config.data_unzip_dir])
            with zipfile.ZipFile(self.config.data_local_data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.data_unzip_dir)
                logger.info(f"{tag}File extracted to: {self.config.data_unzip_dir}")
        else:
            logger.error(f"{tag}The file is not a ZIP file")
            raise ValueError("The file is not a ZIP file")



