import pandas as pd

try:
    df = pd.read_csv("steamgames.csv", na_values='?')
    index_names = df[df['Memória Ram'] > 64].index
    df.drop(index_names, inplace = True)
    index_names = df[df['Espaço em Disco'] > 500].index
    df.drop(index_names, inplace = True)
    df.to_csv("steamgames_output.csv")
    print(index_names)
except Exception as e:
    print(e)

