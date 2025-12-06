from src.coccidiosis_chicken_disease_classifier import logger
from src.coccidiosis_chicken_disease_classifier.pipeline.data_ingestion_staging import DataIngestionPipeline
from src.coccidiosis_chicken_disease_classifier.pipeline.prepare_model_staging import PrepareModelStagingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    data_ingestion_pipeline = DataIngestionPipeline()
    prepare_model_pipeline = PrepareModelStagingPipeline()
    data_ingestion_pipeline.main()
    prepare_model_pipeline.main()
except Exception as e:
    logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
    raise e