from pathlib import Path
from src.e2e_ml_project_1.utils.delete_directories import delete_directories


def clean():
    try:
        # list of paths to delete as Path objects
        # do not delete mlruns folder if the mlflow server is running
        # paths = [Path("artifacts"), Path("logs"), Path("mlruns"), Path("mlartifacts")]
        paths = [Path("artifacts"), Path("logs")]

        # delete the folders
        delete_directories(paths)
        print("Cleaned up the project directories")

    except Exception as e:
        raise e

if __name__ == "__main__":
    clean()