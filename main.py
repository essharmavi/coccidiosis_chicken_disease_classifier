from src.coccidiosis_chicken_disease_classifier import logger
from src.coccidiosis_chicken_disease_classifier.pipeline.data_ingestion_staging import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
except Exception as e:
    logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
    raise e