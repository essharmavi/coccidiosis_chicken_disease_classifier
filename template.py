import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "coccidiosis_chicken_disease_classifier"

list_folders = [
    ".github/workflows/.gitkeep",
    "templates/index.html",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "setup.py",
    "requirements.txt",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/config.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "reasearch/trials.ipynb"
]

for filepath in list_folders:
    filepath_obj = Path(filepath)
    filedir, filename = os.path.split(filepath_obj)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    
    if not filename == "":
        with open(filepath_obj, 'w') as f:
            pass
        logging.info(f"Created file: {filepath_obj}")