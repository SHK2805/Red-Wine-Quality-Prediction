import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

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
            f"src/{project_name}/__init__.py",
            f"src/{project_name}/components/__init__.py",
            f"src/{project_name}/utils/__init__.py",
            f"src/{project_name}/utils/common.py",
            f"src/{project_name}/config/__init__.py",
            f"src/{project_name}/config/configuration.py",
            f"src/{project_name}/pipeline/__init__.py",
            f"src/{project_name}/entity/__init__.py",
            f"src/{project_name}/entity/config_entity.py",
            f"src/{project_name}/constants/__init__.py",
            "config/config.yaml",
            "params.yaml",
            "schema.yaml",
            "main.py",
            "Dockerfile",
            "setup.py",
            "research/research.ipynb",
            "templates/index.html",
            "app.py"
        ]

        for filepath in list_of_files:
            filepath = Path(filepath)
            filedir = filepath.parent

            if filedir != Path():
                os.makedirs(filedir, exist_ok=True)
                logging.info(f"Creating directory {filedir} for the file: {filepath.name}")

            if not filepath.exists() or filepath.stat().st_size == 0:
                filepath.touch()
                logging.info(f"Creating empty file: {filepath}")
            else:
                logging.info(f"{filepath.name} already exists")
    except Exception as e:
        logging.error(f"Error in creating project structure: {e}")
        return False
    return True

if __name__ == "__main__":
    # Define the project name
    ml_project_name = "e2e-ml-project-1"
    # Create the project structure
    create_project_structure(ml_project_name)
