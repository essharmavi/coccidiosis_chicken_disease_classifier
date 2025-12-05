import logging
import sys
import os

logs_dir = "logs"
log_file = os.path.join(logs_dir, "log.log")
os.makedirs(logs_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("coccidiosis_chicken_disease_classifier")
