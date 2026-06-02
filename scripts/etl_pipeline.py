from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/raw")

for csv_file in DATA_DIR.glob("*.csv"):
    print("\n" + "=" * 80)
    print(f"Processing: {csv_file.name}")

    try:
        df = pd.read_csv(csv_file)

        print(f"Shape: {df.shape}")

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print(f"Error reading {csv_file.name}: {e}")