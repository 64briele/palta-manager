import pandas as pd
from pandas import DataFrame

dataset = "dataset/csv/cards.csv"

def load_set(set_code: str) -> DataFrame:
    df = pd.read_csv(dataset)
    df = df.loc[df['setCode'] == set_code]
    return df[['name', 'setCode', 'number', 'quantity']]
