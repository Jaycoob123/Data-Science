import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1 Pobrać i sprawdzić plik

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

try:

    df = pd.read_csv(url)
    print("Dane zostały pomyślnie wczytane!")
except Exception as e:
    print(f"Błąd podczas wczytywania: {e}")
    exit()

print("\n=== KROK 2: WCZESNA EKSPLORACJA DANYCH ===")

print("\n--- Pierwsze 5 wierszy danych: ---")
print(df.head().to_string())

print("\n--- Informacje o danych (dtypes, pamięć, brakujące): ---")
print(df.info())

print("\n--- Liczba brakujących wartości na kolumnę: ---")
missing = pd.DataFrame({
    "liczba_brakow": df.isna().sum(), # Stwórz tabelę/macierz z sumą braków dla każdej kolumny
    "procent_brakow": (df.isna().mean() * 100).round(2)
})

print("\n--- BRAKI DANYCH ---")
print(missing.sort_values("procent_brakow", ascending=False))
# sns.pairplot(df, hue='alive')
# plt.show()

clean = df.copy()

# Kolumna deck ma bardzo dużo braków
clean = clean.drop(columns=["deck"])

# mediana wieku w grupach płeć + klasa biletu
age_median_by_group = clean.groupby(["sex", "pclass"])["age"].transform("median") #Zrób sobie taką tabelkę 'age_median_by_group' weż dane w tabeli 'clean' pogrupuj po płci i klasie. Weź póżniej z tego wiek.
#Weź medianę z tego wieku dla każdej kolumny.
clean["age"]= clean["age"].fillna(age_median_by_group)
# Wejdź w tabelę 'clean', wejdź w kolumnę 'age. Wszędzie, gdzie masz braki wrzuć medianę i nadpisz pod tą samą nazwą
print(age_median_by_group)

# Gdyby jakaś grupa nie miała mediany, uzupełniamy pozostałe braki medianą globalną
clean["age"]= clean["age"].fillna(clean["age"].median())

# 8. Braki w porcie wejścia na statek uzupełniamy dominantą
for col in ["embarked", "embark_town"]:
    most_common_value = clean[col].mode(dropna=True)
    clean[col] = clean[col].fillna(most_common_value)[0]

# 9. Dodajemy zmienną pochodną z NumPy
clean["is_child"] = np.where(clean["age"] < 18, 1, 0)

# 10. Tworzymy przedziały wieku
clean["age_group"] = pd.cut(
    clean["age"],
    bins=[0, 12, 18, 35, 60, np.inf],
    labels=["dziecko","nastolatek", "mlody_dorosly", "dorosly", "senior"],
    right=False
)
print(clean.head().to_string())

# 11. Zmieniamy wybrane kolumny tekstowe/logiczne na typ category.
#     Typ category oszczędza pamięć i jasno pokazuje, że kolumna ma ograniczony zestaw wartości.

categorical_columns = [
    "sex", "embarked", "embark_town", "class", "who", "adult_male", "alive", "alone", "age_group"
]
for col in categorical_columns:
    clean[col] = clean[col].astype("category")

print(clean.head().to_string())
# print(clean["sex"].dtype)
# print(clean["sex"].cat.categories)

# 12. Sprawdzamy duplikaty
duplicates_before = clean.duplicated().sum()
print()
print(f'Liczba duplikatów przed czyszczeniem {duplicates_before}')
clean = clean.drop_duplicates() # funckcja drop_duplicates() usuwa duplikaty

# 13. Kontrola po czyszczeniu
print(f'Braki po czyszczeniu: {clean.isna().sum().sort_values(ascending=False)}')

print("\n--- TYPY DANYCH PO CZYSZCZENIU ---")
print(clean.dtypes)

print("\n--- PRZYKŁADOWE DANE PO CZYSZCZENIU ---")
print(clean.head().to_string())

# 14. Zapisujemy oczyszczony plik
clean.to_csv("titanic_clean.csv", index=False) # Domyślnie program dodaje pierwszą kolumnę z indexem.
# W Index = False oznacza dajemy programowi znać, żeby tego nie robił
print("\nZapisano plik: titanic_clean.csv")