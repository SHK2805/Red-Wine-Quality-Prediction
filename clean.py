# function to delete artifacts and logs folder
import os
import shutil

from src.e2e_ml_project_1.logger.logger_config import logger


def clean():
    try:
        artifacts = "artifacts"
        logs = "logs"
        if os.path.exists(artifacts):
            shutil.rmtree(artifacts)
            logger.info(f"Deleted {artifacts} folder")
        if os.path.exists(logs):
            shutil.rmtree(logs)
            logger.info(f"Deleted {logs} folder")
    except Exception as e:
        logger.error(f"Error deleting folders: {e}")
        raise e

if __name__ == "__main__":
    clean()