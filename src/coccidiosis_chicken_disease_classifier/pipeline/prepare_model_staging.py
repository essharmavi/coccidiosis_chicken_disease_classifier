from src.coccidiosis_chicken_disease_classifier.config.config import PrepareBaseModelConfigManager
from src.coccidiosis_chicken_disease_classifier.components.prepare_base_model import PrepareBaseModel
from src.coccidiosis_chicken_disease_classifier import logger
STAGE_NAME = "Prepare Model Staging Stage"

class PrepareModelStagingPipeline:
    def __init__(self):
        pass

    def main(self):

        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        try:
            config = PrepareBaseModelConfigManager()
            prepare_model_staging_config = config.get_prepare_base_model()

            prepare_model_staging = PrepareBaseModel(config=prepare_model_staging_config)

            prepare_model_staging.get_base_model()
            prepare_model_staging.update_base_model()

            logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
        except Exception as e:
            raise e