import os
import yaml
from src.e2e_ml_project_1.logger.logger_config import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, Dict, List
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    """
    Read the YAML file and return the ConfigBox object
    ConfigBox:
    ConfigBox is a powerful tool that simplifies configuration management in Python projects.
    By centralizing, organizing, and providing easy access to your configuration settings,
    ConfigBox helps you build more maintainable and flexible applications


    :param file_path: Path to the YAML file
    :return: ConfigBox object
    """
    try:
        with open(file_path, "r") as file:
            config = yaml.safe_load(file)
            logger.info(f"The YAML file: {file_path} has been read successfully")
            return ConfigBox(config)
    except BoxValueError as e:
        logger.error(f"Error reading the YAML file: {e}")
        raise ValueError(f"Error reading the YAML file: {e}")
    except Exception as e:
        logger.error(f"Error reading the YAML file: {e}")
        raise e

@ensure_annotations
def create_directories(dirs: list, verbose=True) -> None:
    """
    Create directories if they do not exist

    :param verbose:
    :param dirs: List of directories to create
    :return: None
    """
    for my_dir in dirs:
        if not os.path.exists(my_dir):
            os.makedirs(my_dir, exist_ok=True)
            if verbose:
                logger.info(f"Directory: {my_dir} has been created")
        else:
            if verbose:
                logger.info(f"Directory: {my_dir} already exists")

@ensure_annotations
def save_json(file_path: Path, data: dict) -> None:
    """
    Save the data to the JSON file

    :param file_path: Path to the JSON file
    :param data: Data to save
    :return: None
    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    logger.info(f"Data has been saved to the JSON file: {file_path}")

@ensure_annotations
def load_json(file_path: Path) -> ConfigBox:
    """
    Load the data from the JSON file

    :param file_path: Path to the JSON file
    :return: ConfigBox object
    """
    with open(file_path, "r") as file:
        data = json.load(file)

    logger.info(f"Data has been loaded from the JSON file: {file_path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(file_path: Path, data: Any) -> None:
    """
    Save the data to the binary file

    :param file_path: Path to the binary file
    :param data: Data to save
    :return: None
    """
    joblib.dump(data, file_path)

    logger.info(f"Data has been saved to the binary file: {file_path}")

@ensure_annotations
def load_bin(file_path: Path) -> Any:
    """
    Load the data from the binary file

    :param file_path: Path to the binary file
    :return: Data
    """
    data = joblib.load(file_path)

    logger.info(f"Data has been loaded from the binary file: {file_path}")
    return data

