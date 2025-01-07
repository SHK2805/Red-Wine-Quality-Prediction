from src.e2e_ml_project_1.config.configuration import ConfigurationManager
from src.e2e_ml_project_1.logger.logger_config import logger
from src.e2e_ml_project_1.components.model_trainer import ModelTrainer

STAGE_NAME: str = "Model Training Pipeline"
class ModelTrainingPipeline:
    def __init__(self):
        self.class_name = self.__class__.__name__
        self.stage_name = STAGE_NAME

    def model_trainer(self) -> None:
        tag: str = f"{self.class_name}::model_trainer::"
        try:
            config = ConfigurationManager()
            logger.info(f"{tag}::Configuration Manager object created")

            model_trainer_config = config.get_model_trainer_config()
            logger.info(f"{tag}::Model trainer configuration obtained")

            model_trainer = ModelTrainer(config=model_trainer_config)
            logger.info(f"{tag}::Model trainer object created")

            logger.info(f"{tag}::Running the model training pipeline")

            model_trainer.train_model()
            logger.info(f"{tag}::Model trained successfully")
        except Exception as e:
            logger.error(f"{tag}::Error running the model training pipeline: {e}")
            raise e