import pandas as pd
from pathlib import Path

# 1. Paths
RAW_DATA = Path(r"C:\Users\User\Dev\etl_pipeline_project\data\raw\zara.csv")
PROCESSED_DATA = Path(r"C:\Users\User\Dev\etl_pipeline_project\data\processed\zara_processed.csv")

# 2. Extract
print("Loading raw data...")
df = pd.read_csv(RAW_DATA)

# 3. Transform (mini-cleaning)
print("Cleaning data...")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 4. Load
print("Saving cleaned data...")
df.to_csv(PROCESSED_DATA, index=False)

print("ETL pipeline finished successfully!")
