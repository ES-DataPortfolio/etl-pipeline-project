import pandas as pd
from pathlib import Path

def extract_data(file_path: Path) -> pd.DataFrame:
    print(f"Loading data from {file_path}...")
    return pd.read_csv(file_path, sep=";")