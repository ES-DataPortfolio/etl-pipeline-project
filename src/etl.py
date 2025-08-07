from pathlib import Path
from extract import extract_data
from transform import clean_data
from validate import validate_data
from load import save_data

# 1. Paths
RAW_PATH = Path(r"C:\Users\User\Dev\etl_pipeline_project\data\raw\zara.csv")
PROCESSED_PATH = Path(r"C:\Users\User\Dev\etl_pipeline_project\data\processed\zara_processed.csv")


def run_etl():
    df = extract_data(RAW_PATH)
    df_transform = clean_data(df)
    print(df.columns.tolist())
    validate_data(df_transform)
    save_data(df_transform, PROCESSED_PATH)
    print("ETL pipeline completed successfully!")

if __name__ == "__main__":
    run_etl()