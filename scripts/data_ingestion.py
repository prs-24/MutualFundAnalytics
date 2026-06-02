import pandas as pd
import os

DATA_FOLDER = "data/raw"

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".csv"):

        path = os.path.join(DATA_FOLDER, file)

        print("\n" + "="*60)
        print(f"FILE: {file}")

        df = pd.read_csv(path)

        print(f"Shape: {df.shape}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nHead:")
        print(df.head())