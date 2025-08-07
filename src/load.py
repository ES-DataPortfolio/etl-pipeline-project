from pathlib import Path

def save_data(df, target_path: Path) -> None:
    print(f"Saving cleaned data to {target_path}...")
    df.to_csv(target_path, index=False)