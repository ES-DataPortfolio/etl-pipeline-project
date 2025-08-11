import logging
from pathlib import Path
from config_loader import load_config

# Load config
config = load_config()

# Load Log-Path
LOG_FILE = Path(config["paths"]["log_file"])

# Make sure folder exists
LOG_FILE.parent.mkdir(exist_ok=True, parents=True)

# configure logger
logging.basicConfig(
    level=logging.INFO,  # Info by default
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),  # Log-File
        logging.StreamHandler()  # additionally printing to console (optional)
    ]
)

# create logger
logger = logging.getLogger(__name__)

