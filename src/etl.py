from pathlib import Path
from extract import extract_data
from transform import clean_data
from validate import validate_data
from load import save_data
from config_loader import load_config
from logger import logger

#def load_config():
#    CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.yaml"
#    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
#       return yaml.safe_load(f)

# 1. loading paths from config.yaml
#RAW_PATH = Path(config["paths"]["raw_data"])

config = load_config()

RAW_PATH = Path(__file__).resolve().parent.parent / "data" / "raw" / "zara.csv"
PROCESSED_PATH = Path(__file__).resolve().parent.parent / "data" / "processed" / "zara_processed.csv"

def run_etl():
    logger.info("Starting ETL pipeline...")

    # Extract
    df = extract_data(RAW_PATH)
    logger.info("Data extraction completed.")

    # Transform
    df_transform = clean_data(df)
    logger.info("Data transformation completed.")

    # Validate
    if not validate_data(df_transform):
        print("ETL aborted due to validation errors.")
        logger.error("ETL aborted due to validation errors.")
        return

    # Load
    save_data(df_transform, PROCESSED_PATH)
    logger.info("Data loaded successfully.")
    logger.info("ETL pipeline completed successfully!")

if __name__ == "__main__":
    run_etl()
