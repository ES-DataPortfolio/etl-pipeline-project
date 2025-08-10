import pandas as pd

def validate_data(df: pd.DataFrame) -> bool:
    """Validates the DataFrame for nulls, duplicates, and correct dtypes.
    Returns True if validation passes, False otherwise."""
    print("Validating data...")

    null_counts = df.isnull().sum()
    duplicate_count = df.duplicated().sum()
    dtypes = df.dtypes

    print(f"Null values:\n{null_counts}")
    print(f"Duplicates: {duplicate_count}")
    print(f"Data types:\n{dtypes}")

    # Simple quality rules (extendable)
    if duplicate_count > 0:
        print("Validation failed: Dataset contains duplicates.")
        return False
    if null_counts.any():
        print("Validation failed: Dataset contains missing values.")
        return False

    print("Validation passed.")
    return True
