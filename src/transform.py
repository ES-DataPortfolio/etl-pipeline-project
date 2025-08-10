import pandas as pd
from config_loader import load_config

config = load_config()

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    print("Cleaning data...")

    # 1. clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # 2. critical fields: drop if empty
    #critical_fields = ["product_id", "sales_volume", "price"] redundant due to config
    df = df.dropna(subset=config["etl"]["drop_na_columns"], how="any")

    # 3. fix datatypes
    df["sales_volume"] = pd.to_numeric(df["sales_volume"], errors="coerce")
    df["scraped_at"] = pd.to_datetime(df["scraped_at"], errors="coerce").dt.strftime(config["etl"]["date_format"])

    # 4. non-critical fields: fill with "Unknown" if empty 
    text_columns = df.select_dtypes(include=["object"]).columns
    for col in text_columns:
        df[col] = df[col].fillna(config["etl"]["fill_text_with"])

    # 5. Fill numeric columns
    numeric_columns = df.select_dtypes(include=["number"]).columns
    df[numeric_columns] = df[numeric_columns].fillna(config["etl"]["fill_numeric_with"])

    # 6. if any nulls left -> fill with "Unknown"
    df = df.fillna("Unknown")

    return df
