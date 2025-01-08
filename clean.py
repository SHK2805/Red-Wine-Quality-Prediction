from pathlib import Path
from src.e2e_ml_project_1.utils.delete_directories import delete_directories


def clean(clean_artifacts: bool = False):
    try:
        # list of paths to delete as Path objects
        # do not delete mlruns folder if the mlflow server is running
        if clean_artifacts:
            paths = [Path("artifacts"), Path("logs"), Path("mlruns"), Path("mlartifacts")]
        else:
            paths = [Path("artifacts"), Path("logs")]

        # delete the folders
        delete_directories(paths)
        print("Cleaned up the project directories")

    except Exception as e:
        raise e

if __name__ == "__main__":
    # set to True to clean up all artifacts, logs and mlflow folders
    # if deleting the mlflow folders then make sure mlflow server is not running
    # make sure the Flask app is not running
    clean(True)