import pandas as pd

try:
    df = pd.read_csv("steamgames.csv", na_values='?')
    index_names = df[df['Quantidade de Review'] <=  50 ].index
    df.drop(index_names, inplace = True)
    print(df.shape)
    df.to_csv("steamgames_output.csv")
except Exception as e:
    print(e)