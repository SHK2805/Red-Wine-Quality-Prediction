from clean import clean
from src.e2e_ml_project_1.logger.logger_config import logger
from src.e2e_ml_project_1.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.e2e_ml_project_1.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.e2e_ml_project_1.pipeline.data_validation import DataValidationTrainingPipeline
from src.e2e_ml_project_1.pipeline.model_evaluation import ModelEvaluationTrainingPipeline
from src.e2e_ml_project_1.pipeline.model_trainer import ModelTrainerTrainingPipeline


class RunPipeline:
    def __init__(self):
        self.class_name = self.__class__.__name__
        self.data_ingestion_pipeline: DataIngestionTrainingPipeline = DataIngestionTrainingPipeline()
        self.data_validation_pipeline: DataValidationTrainingPipeline = DataValidationTrainingPipeline()
        self.data_transformation_pipeline: DataTransformationTrainingPipeline = DataTransformationTrainingPipeline()
        self.model_trainer_pipeline: ModelTrainerTrainingPipeline = ModelTrainerTrainingPipeline()
        self.model_evaluation_pipeline: ModelEvaluationTrainingPipeline = ModelEvaluationTrainingPipeline()

    def run_data_ingestion_pipeline(self) -> None:
        tag: str = f"{self.class_name}::run_data_ingestion_pipeline::"
        try:
            logger.info(f"[STARTED]>>>>>>>>>>>>>>>>>>>> {self.data_ingestion_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<")
            logger.info(f"{tag}::Running the data ingestion pipeline")
            self.data_ingestion_pipeline.data_ingestion()
            logger.info(f"{tag}::Data ingestion pipeline completed")
            logger.info(f"[COMPLETE]>>>>>>>>>>>>>>>>>>>> {self.data_ingestion_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<\n\n\n")
        except Exception as e:
            logger.error(f"{tag}::Error running the data ingestion pipeline: {e}")
            raise e

    def run_data_validation_pipeline(self) -> None:
        tag: str = f"{self.class_name}::run_data_validation_pipeline::"
        try:
            logger.info(f"[STARTED]>>>>>>>>>>>>>>>>>>>> {self.data_validation_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<")
            logger.info(f"{tag}::Running the data validation pipeline")
            self.data_validation_pipeline.data_validation()
            logger.info(f"{tag}::Data validation pipeline completed")
            logger.info(f"[COMPLETE]>>>>>>>>>>>>>>>>>>>> {self.data_validation_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<\n\n\n")
        except Exception as e:
            logger.error(f"{tag}::Error running the data validation pipeline: {e}")
            raise e

    def run_data_transformation_pipeline(self) -> None:
        tag: str = f"{self.class_name}::run_data_transformation_pipeline::"
        try:
            logger.info(f"[STARTED]>>>>>>>>>>>>>>>>>>>> {self.data_transformation_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<")
            logger.info(f"{tag}::Running the data transformation pipeline")
            self.data_transformation_pipeline.data_transformation()
            logger.info(f"{tag}::Data transformation pipeline completed")
            logger.info(f"[COMPLETE]>>>>>>>>>>>>>>>>>>>> {self.data_transformation_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<\n\n\n")
        except Exception as e:
            logger.error(f"{tag}::Error running the data transformation pipeline: {e}")
            raise e

    def run_model_trainer_pipeline(self) -> None:
        tag: str = f"{self.class_name}::run_model_training_pipeline::"
        try:
            logger.info(f"[STARTED]>>>>>>>>>>>>>>>>>>>> {self.model_trainer_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<")
            logger.info(f"{tag}::Running the model training pipeline")
            self.model_trainer_pipeline.model_trainer()
            logger.info(f"{tag}::Model training pipeline completed")
            logger.info(f"[COMPLETE]>>>>>>>>>>>>>>>>>>>> {self.model_trainer_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<\n\n\n")
        except Exception as e:
            logger.error(f"{tag}::Error running the model training pipeline: {e}")
            raise e

    def run_model_evaluation_pipeline(self) -> None:
        tag: str = f"{self.class_name}::run_model_evaluation_pipeline::"
        try:
            logger.info(f"[STARTED]>>>>>>>>>>>>>>>>>>>> {self.model_evaluation_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<")
            logger.info(f"{tag}::Running the model evaluation pipeline")
            self.model_evaluation_pipeline.model_evaluation()
            logger.info(f"{tag}::Model evaluation pipeline completed")
            logger.info(f"[COMPLETE]>>>>>>>>>>>>>>>>>>>> {self.model_evaluation_pipeline.stage_name} <<<<<<<<<<<<<<<<<<<<\n\n\n")
        except Exception as e:
            logger.error(f"{tag}::Error running the model evaluation pipeline: {e}")
            raise e

    """
    # before running the model evaluation pipeline,
    # make sure the mlflow server is running
    # and the correct mlflow uri is set in the config file config.yaml
    # add mlflow to the requirements.txt file or
    # install it manually using pip install mlflow
    # run the mlflow server using
    # mlflow server --host 127.0.0.1 --port 8080
    """
    def run(self):
        self.run_data_ingestion_pipeline()
        self.run_data_validation_pipeline()
        self.run_data_transformation_pipeline()
        self.run_model_trainer_pipeline()
        self.run_model_evaluation_pipeline()

if __name__ == "__main__":
    # Run the pipelines
    run_pipeline = RunPipeline()
    run_pipeline.run()
