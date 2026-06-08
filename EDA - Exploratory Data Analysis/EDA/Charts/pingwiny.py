import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# Wyświetlenie pierwszych 5 wierszy
print(penguins)
print(type(penguins))

sns.pairplot(penguins, hue='species')
plt.show()

print('\nDescribe:')
print(df.describe().T.round(2).to_string())
print(f'Nazwy kolumn: {penguins.columns}')
penguins_filtered = penguins.drop(columns=['island', 'sex' ].dropna)