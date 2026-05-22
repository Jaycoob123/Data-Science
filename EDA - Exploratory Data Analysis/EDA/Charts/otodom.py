import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('otodom.csv')
print(df)

print('\nDescribe:')
print(df.describe().T.round(2).to_string())

sns.histplot(df.cena)
plt.show()
plt.scatter(df.cena, df.powierzchnia)
plt.show()