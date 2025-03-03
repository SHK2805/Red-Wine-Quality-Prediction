import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

def create_project_structure(project_name: str) -> bool:
    try:
        # Define the list of files and directories to create
        list_of_files = [
            # general files
            "template.py",
            ".gitignore",
            ".dockerignore",
            "requirements.txt",
            "README.md",
            "data_description.md",
            ".github/workflows/.gitkeep",
            # log files
            f"logs/",
            f"src/{project_name}/__init__.py",
            # components
            f"src/{project_name}/components/__init__.py",
            f"src/{project_name}/components/data_cleaning.py",
            f"src/{project_name}/components/data_ingestion.py",
            f"src/{project_name}/components/data_validation.py",
            f"src/{project_name}/components/data_transformation.py",
            f"src/{project_name}/components/model_trainer.py",
            f"src/{project_name}/components/model_evaluation.py",
            # logger
            f"src/{project_name}/logger/__init__.py",
            f"src/{project_name}/logger/logger_config.py",
            # utils
            f"src/{project_name}/utils/__init__.py",
            f"src/{project_name}/utils/common.py",
            f"src/{project_name}/utils/schema_manager.py",
            f"src/{project_name}/utils/delete_directories.py",
            # config
            f"src/{project_name}/config/__init__.py",
            f"src/{project_name}/config/configuration.py",
            # pipeline
            f"src/{project_name}/pipeline/__init__.py",
            f"src/{project_name}/pipeline/data_ingestion.py",
            f"src/{project_name}/pipeline/data_validation.py",
            f"src/{project_name}/pipeline/data_transformation.py",
            f"src/{project_name}/pipeline/model_trainer.py",
            f"src/{project_name}/pipeline/model_evaluation.py",
            f"src/{project_name}/pipeline/prediction.py",
            # entity
            f"src/{project_name}/entity/__init__.py",
            f"src/{project_name}/entity/config_entity.py",
            # constants
            f"src/{project_name}/constants/__init__.py",
            f"src/{project_name}/constants/constants.py",
            # config, params, schema
            "config/config.yaml",
            "params.yaml",
            "schema.yaml",
            # research
            "research/research.ipynb",
            "research/research.py",
            "research/__init__.py",
            # other files
            "main.py",
            "Dockerfile",
            "setup.py",
            # app
            "templates/index.html",
            "templates/results.html",
            "app.py",
            # clean
            "clean.py"
        ]

        for filepath in list_of_files:
            filepath = Path(filepath)
            filedir = filepath.parent

            # Create directories
            if filedir != Path():
                os.makedirs(filedir, exist_ok=True)
                logging.info(f"Creating directory {filedir} for the file: {filepath.name}")

            # Create files if they do not exist or are empty
            if filepath.suffix:  # Check if it's a file (has a suffix)
                if not filepath.exists() or filepath.stat().st_size == 0:
                    filepath.touch()
                    logging.info(f"Creating empty file: {filepath}")
                else:
                    logging.info(f"{filepath.name} already exists")
            else:
                if not filepath.exists():  # Create directory if it doesn't exist
                    os.makedirs(filepath, exist_ok=True)
                    logging.info(f"Creating directory: {filepath}")
                else:
                    logging.info(f"Directory {filepath} already exists")
    except Exception as e:
        logging.error(f"Error in creating project structure: {e}")
        return False
    return True

if __name__ == "__main__":
    # Define the project name
    # This will be the name of the project directory
    # The name cannot have spaces or special characters except for underscores
    ml_project_name = "red_wine_quality_prediction"
    # Create the project structure
    create_project_structure(ml_project_name)
    logging.info(f"Project structure created for {ml_project_name}")