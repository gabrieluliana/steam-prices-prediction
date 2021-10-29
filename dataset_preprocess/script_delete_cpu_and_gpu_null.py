import pandas as pd
import numpy as np

try:
    df = pd.read_csv("steamgames.csv", na_values=False)
    index_names = df[df['Placa de Vídeo'].isna()].index
    df.drop(index_names, inplace = True)
    index_names = df[df['Processador'].isna()].index
    df.drop(index_names, inplace = True)
    print(df.describe())
    df.to_csv("steamgames_output.csv")
except Exception as e:
    print(e)