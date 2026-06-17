import pandas as pd


def load_data(path):

    df = pd.read_csv(path)

    return df


def clean_data(df):

    # remove duplicates
    df = df.drop_duplicates()


    # remove impossible values

    df = df[df["price"] > 0]

    df = df[df["bedrooms"] > 0]


    # remove extreme price outliers

    lower = df["price"].quantile(0.01)
    upper = df["price"].quantile(0.99)


    df = df[
        (df["price"] >= lower) &
        (df["price"] <= upper)
    ]


    return df


def create_features(df):

    # convert date

    df["date"] = pd.to_datetime(
        df["date"]
    )


    df["sale_year"] = (
        df["date"].dt.year
    )


    df["sale_month"] = (
        df["date"].dt.month
    )


    # house age

    current_year = 2025

    df["house_age"] = (
        current_year - df["yr_built"]
    )


    # renovated indicator

    df["renovated"] = (
        df["yr_renovated"] > 0
    ).astype(int)


    return df