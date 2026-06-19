import pandas as pd

def load_raw_data(path="data/raw/kc_house_data.csv"):
    return pd.read_csv(path)