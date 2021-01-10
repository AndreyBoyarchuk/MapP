import pandas as pd
import numpy as np

df = pd.read_csv('83709.csv')

maxD=df.iloc[df.groupby('NAME')['ELEV'].agg(pd.Series.idxmax)]
minDD=df.iloc[df.groupby('NAME')['ELEV'].agg(pd.Series.idxmin)]
print(maxD)
print(minDD)