from src.coccidiosis_chicken_disease_classifier import logger
from src.coccidiosis_chicken_disease_classifier.components.data_ingestion import DataIngestion
from src.coccidiosis_chicken_disease_classifier.config.config import ConfigManager


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline():
    def __init__(self):
        pass

    def main(self):

        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        try:
            config = ConfigManager()
            data_ingestion_config = config.get_data_ingestion_config()

            data_ingestion = DataIngestion(config=data_ingestion_config)

            data_ingestion.download_file()

            data_ingestion.extract_zip_file()

            logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
        except Exception as e:
            raise e




