import pandas as pd


def normalize(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip().lower()