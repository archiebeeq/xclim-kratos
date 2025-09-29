import pandas as pd
import numpy as np

REQUIRED_COLS = ["year", "month", "day", "prec", "tmax", "tmin"]

def read_csv_to_df(path):
    """Read 6-column CSV (year,month,day,prec,tmax,tmin) -> pandas DataFrame."""
    df = pd.read_csv(path, header=0, dtype=str)
    df.columns = [c.strip().lower() for c in df.columns]
    if not set(REQUIRED_COLS).issubset(df.columns):
        missing = set(REQUIRED_COLS) - set(df.columns)
        raise ValueError(f"Missing required columns: {missing}")
    # coerce numeric
    for col in ["year", "month", "day"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype('Int64')
    for col in ["prec", "tmax", "tmin"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    # drop rows missing date parts
    df = df.dropna(subset=["year", "month", "day"]).reset_index(drop=True)
    return df
