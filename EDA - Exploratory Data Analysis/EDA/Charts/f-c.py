import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv('f-c.csv',usecols=[1, 2])
print(df)

model = Squential()
model.add(Dense(1, activation='linear'))
model.add(Dense(2, activation='linear'))
model.add(Dense(2, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='rmsprop', loss='mse')

result = model.fit(df.F, df.C, epochs=300)

model.predict(df.F)

# wykres 1  F -> C
# wykres 2  F -> C_pred

C_pred = model.predict(df.F)

plt.scatter(df.F, )