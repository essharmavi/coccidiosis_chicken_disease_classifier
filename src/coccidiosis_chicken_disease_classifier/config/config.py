import os
from src.coccidiosis_chicken_disease_classifier.constants import *
from src.coccidiosis_chicken_disease_classifier.utils.common import read_yaml, create_directories
from src.coccidiosis_chicken_disease_classifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbacksConfig


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
    


class PrepareBaseModelConfigManager:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, parmas_file_path=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)

        create_directories(self.config.artifacts_root)

    def get_prepare_base_model(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories(config.root_dir)

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_classes=self.params.CLASSES,
            params_image_size=self.params.IMAGE_SIZE,
            params_include_top=self.params.INCLUDE_TOP,
            params_learning_rate=self.params.LEARNING_RATE,
            params_weights=self.params.WEIGHTS,
        )

        return prepare_base_model_config
    

class PrepareCallbacksConfigManager:
    def __init__(self, config_file_path: Path = CONFIG_FILE_PATH, parmas_file_path: Path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(parmas_file_path)
        
        create_directories(self.config.artifacts_root)

    def get_prepare_callbacks(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks

        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories(model_ckpt_dir)
        create_directories(config.tensorboard_root_log_dir)

        return PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_dir=Path(config.checkpoint_model_filepath))