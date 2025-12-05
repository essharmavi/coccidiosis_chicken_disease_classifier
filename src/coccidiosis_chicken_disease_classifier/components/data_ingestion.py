
import os
import zipfile
from pathlib import Path
from urllib.request import urlretrieve
from src.coccidiosis_chicken_disease_classifier import logger
from src.coccidiosis_chicken_disease_classifier.utils.common import get_size
from src.coccidiosis_chicken_disease_classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urlretrieve(
                url=self.config.source_URL, filename=self.config.local_data_file
            )
            logger.info(
                f"{filename} downloaded successfully and saved in {self.config.local_data_file}"
            )
        else:
            logger.info(
                f"File already exists in {self.config.local_data_file} with size {get_size(file_path=Path(self.config.local_data_file))}"
            )

    def extract_zip_file(self):
        unzip_filepath = self.config.unzipped_data_dir
        print(unzip_filepath,self.config.local_data_file,)
        os.makedirs(unzip_filepath, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_file:
            zip_file.extractall(unzip_filepath)