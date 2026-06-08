import pandas as pd
import numpy as np

df = pd.read_csv('diabetes.csv')
print(df)

print(f'Kształt danych: {df.shape}')
print('\nDescribe:')
print(df.describe().T.round(2).to_string())

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin', 'bmi', 'diabetespedigreefunction', 'age']:

    df[col] = df[col].replace(0, np.nan)

    mean_= df[col].mean
    df[col] = df[col].replace(np.nan, mean_)

print('\nPo oczyszczaniu:')
print(df.describe().T.round(2).to_string())