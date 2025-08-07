import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    print("Cleaning data...")

    # Spaltennamen vereinheitlichen
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Fehlende Werte behandeln
    df = df.dropna(subset=["product_id", "sales_volume", "price"], how="any")

    # Datentypen korrigieren
    df["sales_volume"] = pd.to_numeric(df["sales_volume"], errors="coerce")
    df["scraped_at"] = pd.to_datetime(df["scraped_at"], errors="coerce").dt.date

    return df