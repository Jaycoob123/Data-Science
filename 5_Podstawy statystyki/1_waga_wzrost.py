# Cele zadania:
# 1. Przeliczyć wzrost i wagę na jednostki metryczne.
# 2. Porównać wzrost kobiet i mężczyzn.
# 3. Policzyć podstawowe statystyki opisowe.
# 4. Policzyć 95% przedział ufności dla średniego wzrostu.
# 5. Zinterpretować wyniki.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('2_EDA/data/weight-height.csv', sep=";")
print(df)
print(df.head())

df["Height_cm"] = df["Height"] * 2.54
df["Weight_kg"] = df["Weight"] / 2.2

# porównanie grup
kobiety = df[df["Gender"] == "Female"]
mezczyzni = df[df["Gender"] == "Male"]
wzrost_kobiety = kobiety["Height_cm"]
wzrost_mezczyzni = mezczyzni["Height_cm"]

### STATYSTYKI OPISOWE
# ŚREDNIA:
# MEDIANA:
# WARIANCJA:
# ODCHYLENIE STANDARDOWE:
print("\n---KOBIETY---")
print("Liczba obserwacji:", len(wzrost_kobiety))
print("Średnia:", wzrost_kobiety.mean())
print("Mediana:", wzrost_kobiety.median())
print("Wariancja:", wzrost_kobiety.var())
print("Odchylenie standardowe:", wzrost_kobiety.std())

print("\n---MEZCZYZNI---")
print("Liczba obserwacji:", len(wzrost_mezczyzni))
print("Średnia:", wzrost_mezczyzni.mean())
print("Mediana:", wzrost_mezczyzni.median())
print("Wariancja:", wzrost_mezczyzni.var())
print("Odchylenie standardowe:", wzrost_mezczyzni.std())

### PRZEDZIAŁ UFNOŚCI DLA ŚREDNIEJ

def przedzial_ufnosci_95(dane): 
    srednia = dane.mean()
    odchylenie = dane.std()
    n = len(dane)
    blad_standardowy = odchylenie / (n ** 0.5)
    t_krytyczne = stats.t.ppf(0.975, df=n - 1)
    dolna_granica = srednia - t_krytyczne * blad_standardowy
    gorna_granica = srednia + t_krytyczne * blad_standardowy
    return dolna_granica, gorna_granica

# Przedział, w którym na 95% znajduje się średnia dla wzrostu kobiet i mężczyzn
ci_kobiety = przedzial_ufnosci_95(wzrost_kobiety)
ci_mezczyzni = przedzial_ufnosci_95(wzrost_mezczyzni)

print("\n95% przedział ufności dla średniego wzrostu kobiet:")
print(ci_kobiety)

print("\n95% przedział ufności dla średniego wzrostu mężczyzn:")
print(ci_mezczyzni)

plt.hist(wzrost_mezczyzni, bins=300, label='Men_Height', alpha=0.5)
plt.hist(wzrost_kobiety, bins=300, label='Women_Height', alpha=0.5)
plt.title("Height Distribution Men & Women")
plt.xlabel("Height_cm")
plt.ylabel("Number of People")
plt.legend(loc='upper right')
plt.show()

plt.bar(["Women", "Men"], [przedzial_ufnosci_95(wzrost_kobiety), przedzial_ufnosci_95(wzrost_mezczyzni)])
plt.title("CI Gender Comparison")
plt.xlabel("Gender")
plt.ylabel("Height (cm)")
plt.show()

# Trening:
# Policz analogiczny 95% przedział ufności dla średniej wagi kobiet i mężczyzn.
# Sprawdź, jak zmieni się szerokość przedziału ufności, jeżeli użyjesz tylko losowych 100 obserwacji z każdej grupy. Wyjaśnij, dlaczego przedział zrobił się szerszy albo węższy.