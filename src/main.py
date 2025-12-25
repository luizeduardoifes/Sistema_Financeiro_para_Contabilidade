import pandas as pd

df = pd.read_excel("data/raw/lancamentos.xlsx", engine="openpyxl")

df.columns = df.columns.str.lower()

df["data"] = pd.to_datetime(df["data"])

tipos_validos = ["receita", "despesa"]
if not df["tipo"].isin(tipos_validos).all():
    raise ValueError("Erro: coluna 'tipo' inválida")

df["mes"] = df["data"].dt.to_period("M")

df.to_excel("data/processed/lancamentos_tratados.xlsx",index= False)

print("Base preparada com sucesso!")