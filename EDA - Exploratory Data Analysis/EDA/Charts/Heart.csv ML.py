import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('heart.csv')
print(df)

print('\nDescribe:')
prin(df.describe().T.round(2).to_string())