from research.ml_research import ConfigurationManager, DataIngestion
from src.e2e_ml_project_1.logger.logger_config import logger


def run_data_ingestion() -> None:
    try:
        tag: str = "run_data_ingestion"
        config = ConfigurationManager()
        logger.info(f"{tag}::Configuration Manager object created")

        data_ingestion_config = config.get_data_ingestion_config()
        logger.info(f"{tag}::Data ingestion configuration obtained")

        data_ingestion = DataIngestion(data_ingestion_config)
        logger.info(f"{tag}::Data ingestion object created")

        logger.info(f"{tag}::Running the data ingestion pipeline")

        data_ingestion.download_file()
        logger.info(f"{tag}::Data downloaded successfully")

        data_ingestion.extract_file()
        logger.info(f"{tag}::Data extracted successfully")

        return



    except Exception as e:
        logger.error(f"Error running the data ingestion pipeline: {e}")
        raise e

if __name__ == "__main__":
    # Run the data ingestion pipeline
    # when you run this script, the data ingestion pipeline will be executed
    # add some dummy values to the params.yaml file and schema.yaml file to avoid the file empty error
    # Example data key: value
    run_data_ingestion()