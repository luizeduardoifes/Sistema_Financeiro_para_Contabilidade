import pandas as pd

df = pd.read_excel("data/raw/lancamentos.xlsx")

df.columns = df.columns.str.lower()

df["data"] = pd.to_datetime(df["data"])