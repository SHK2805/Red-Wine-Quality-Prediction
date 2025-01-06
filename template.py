import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

def create_project_structure(project_name: str) -> bool:
    try:
        # Define the list of files and directories to create
        list_of_files = [
            ".gitignore",
            ".dockerignore",
            "requirements.txt",
            "README.md",
            "template.py",
            ".github/workflows/.gitkeep",
            f"logs/",
            f"src/{project_name}/__init__.py",
            f"src/{project_name}/components/__init__.py",
            f"src/{project_name}/logger/__init__.py",
            f"src/{project_name}/logger/logger_config.py",
            f"src/{project_name}/utils/__init__.py",
            f"src/{project_name}/utils/common.py",
            f"src/{project_name}/config/__init__.py",
            f"src/{project_name}/config/configuration.py",
            f"src/{project_name}/pipeline/__init__.py",
            f"src/{project_name}/entity/__init__.py",
            f"src/{project_name}/entity/config_entity.py",
            f"src/{project_name}/constants/__init__.py",
            f"src/{project_name}/constants/constants.py",
            "config/config.yaml",
            "params.yaml",
            "schema.yaml",
            "main.py",
            "Dockerfile",
            "setup.py",
            "research/research.ipynb",
            "research/my_research.py",
            "research/research_run.py",
            "research/__init__.py",
            "templates/index.html",
            "app.py"
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
    ml_project_name = "e2e_ml_project_1"
    # Create the project structure
    create_project_structure(ml_project_name)
    logging.info(f"Project structure created for {ml_project_name}")