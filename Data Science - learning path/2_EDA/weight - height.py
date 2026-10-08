import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/weight-height.csv', sep=';')
print(df)

# df['Height2'] = df.Height * 2.54 #nowa kolumna
# df['Height'] = df.Height * 2.54 # nadpisanie kolumny
df['Height'] *= 2.54 # Wejdź w kolumnę 'Height' pomnóż ją przez 2.54 (cale na cm) i zapisz pod tą samą nazwą
df['Weight'] /= 2.2 # Wejdź w kolumnę 'Weight' podziel ją przez 2.2 (funty na kilogramy) i zapisz pod tą samą nazwą

print('\ndescribe:')
print(df.describe().T.round(2).to_string())

plt.hist(df.query("Gender== 'Male'")['Weight'], bins=30)
plt.hist(df.query("Gender== 'Female'")['Weight'], bins=30)
plt.show()

sns.histplot(df.query("Gender== 'Male'")['Weight'])
sns.histplot(df.query("Gender== 'Female'")['Weight'])
plt.show()
