import os.path
import urllib.request as request
import zipfile
from src.e2e_ml_project_1.entity.config_entity import DataIngestionConfig
from src.e2e_ml_project_1.logger.logger_config import logger
from src.e2e_ml_project_1.utils.common import create_directories


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