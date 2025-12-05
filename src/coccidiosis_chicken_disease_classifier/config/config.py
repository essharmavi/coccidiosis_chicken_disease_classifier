from src.coccidiosis_chicken_disease_classifier.constants import *
from src.coccidiosis_chicken_disease_classifier.utils.common import read_yaml, create_directories
from src.coccidiosis_chicken_disease_classifier.entity.config_entity import DataIngestionConfig


class ConfigManager:
    def __init__(self, config_filepath: Path = CONFIG_FILE_PATH, params_filepath: Path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories(path= Path(self.config.artifacts_root))

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories(path= Path(config.root_dir))

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzipped_data_dir= config.unzipped_data_dir
        )

        return data_ingestion_config