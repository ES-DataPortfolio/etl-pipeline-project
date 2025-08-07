import pandas as pd

def validate_data(df: pd.DataFrame) -> None:
    print("Validating data...")
    print(f"Null values:\n{df.isnull().sum()}")
    print(f"Duplicates: {df.duplicated().sum()}")
    print(f"Data types:\n{df.dtypes}")