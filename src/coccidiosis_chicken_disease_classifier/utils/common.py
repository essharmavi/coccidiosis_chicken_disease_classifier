import os
import yaml
import json
import base64
import joblib
from typing import Any
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from src.coccidiosis_chicken_disease_classifier import logger


def read_yaml(yaml_path: Path) -> ConfigBox:
    """
    Docstring for read_yaml
    """
    try:
        with open(yaml_path, "r") as f:
            content = yaml.safe_load(f)
            logger.info(f"YAML file: {yaml_path} loaded successfully")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("File is empty")
    except Exception as e:
        raise e


def create_directories(path: Path):
    """
    Docstring for create_directories
    """
    os.makedirs(path, exist_ok=True)
    logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Docstring for save_json
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Docstring for load_json
    """
    with open(path, "r") as f:
        content = json.load(f)
    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Docstring for save_bin
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Docstring for load_bin
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


def decodeImage(image_string, fileName: str) -> bytes:
    """
    Docstring for decodeImage
    """
    image_bytes = base64.b64decode(image_string)
    with open(fileName, "wb") as fh:
        fh.write(image_bytes)
        f.close()
    logger.info(f"Image decoded and saved to file: {fileName}")
    return image_bytes

def encodeImage(cropped_image_path) -> str:
    """
    Docstring for encodeImage
    """
    with open(cropped_image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string
    logger.info(f"Image at {cropped_image_path} encoded to base64 string")


def get_size(file_path: Path) -> str:
    size = round(os.path.getsize(filename=file_path)/1024)
    return f"{size} kb"