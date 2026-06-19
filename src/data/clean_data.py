import numpy as np
import pandas as pd

def clean_housing_data(df):
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna(subset=["lat", "long"])

    df["log_price"] = np.log1p(df["price"])
    df["house_age"] = df["date"].dt.year - df["yr_built"]

    low, high = df["log_price"].quantile([0.01, 0.99])
    df = df[(df["log_price"] >= low) & (df["log_price"] <= high)]

    return df.reset_index(drop=True)