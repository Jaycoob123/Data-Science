import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import alpha

# 1. pobieranie danych

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-31/beers.csv"

try:
    df = pd.read_csv(url)
    print('dane pobrane')
except Exception as e:
    print(f'Bląd {e}')
    print('Uzywam danych zapasowych')
    data = {
        'nazwa': ['IPA','IPA', 'Lager', 'Stout', 'Pilsner', 'Wheat', 'Porter', 'Ale', 'Bock'],
        'alkohol': [6.5, 6.5, 5.0, 7.2, 4.8, 5.2, 5.8, 5.5, 6.8],
        'goryczka': [65, 65, np.nan, 45, 30, 15, 40, 35, 25],
        'ocena': [4.2, 4.2, 3.8, 4.5, 3.9, 3.7, 4.1, 4.0, 4.3],
        'styl': ['IPA', 'IPA', 'Lager', 'Ciemne', 'Lager', np.nan, 'Ciemne', 'Jasne', 'Ciemne']
    }
    df = pd.DataFrame(data)

# 2. Podstawowe info
print('\n' + '='*50) # \n - to oznacza enter, czyli zacznij od nowej linijki
print(f'Wymiary danych: {df.shape}')
print(f'Liczba wierszy: {df.shape[0]}')
print(f'Liczba kolumn: {df.shape[1]}')

# 3. Podgląd danych
print('\nPierwsze 5 piw\n')
print(df.head())
print('\nOstatnie 3 piwa\n')
print(df.tail(3))

# 4. Typy danych
print(f'\n{df.info()}')

# 5. Statystyki numeryczne
kolumny_numeryczne = df.select_dtypes(include='number').columns # nazwy kolumn numerycznych
if len(kolumny_numeryczne) > 0:
    print('Statystyki dla cech numerycznych')
    print(df[kolumny_numeryczne].describe().T.to_string()) # Wejdź w df i wybierz tylko 'kolumny_numeryczne' i z tego zrób describe
else:
    print('Brak kolumn numerycznych w danych')

# 6. Statystyki kategoryczne

print("\n" + "="*50)
print("STATYSTYKI KATEGORYCZNE")
print("="*50)

kolumny_tekstowe = df.select_dtypes(include='str').columns
if len (kolumny_tekstowe) > 0:
    for kolumna in kolumny_tekstowe:
        print(f'\nKolumna: {kolumna}')
        print(f'Liczba unikalnych wartosci: {df[kolumna].unique()}')
        print('3 najczęstsze wartości')
        print(df[kolumna].value_counts().head(3))

else:
    print('Brak kolumn kategorycznych w danych')

# 7. Brakujące wartości

print("\n" + "=" * 50)
print("BRAKUJĄCE WARTOŚCI")
print("=" * 50)

brakujace = df.isnull().sum()
if brakujace.sum() > 0:
    print('Kolumny z brakujacymi wartosciami:')
    for kolumna in df.columns: # Jeżeli (if), gdzięś znalazłeś braki, przeleć przez każdą kolumnę i jeżeli w tej danej kolumnie
        if df[kolumna].isnull().sum() > 0:
            braki_liczbowo = df[kolumna].isnull().sum()
            braki_procentowo = braki_liczbowo / len(df) * 100
            print(f'    {kolumna}: {braki_liczbowo} ({braki_procentowo: .1f})%')
# print("\n" + "=" *50)
# print("TWORZENIE WYKRESÓW")
# print("=" * 50)

# # wykres 1, rozklad zawartości alkoholu
# if 'alkohol' in df.columns:
#     plt.figure(figsize=(10, 6))
#     plt.subplot(1, 2, 1) # jeden wiersz, 2 kolumny, pierwszy z lewej
#     df['alkohol'].hist (bins=10, color='lightblue', edgecolor='black')
#     plt.title('Rozklad zawartosci alkoholu')
#     plt.xlabel('Zawartosc alko w (%)')
#     plt.ylabel('Liczba piw')
#     plt.subplot(1, 2, 2)
#     df.boxplot(column='alkohol', grid=False)
#     plt.title('Boxplot: Zawartość alkoholu')
#     plt.tight_layout()
#     plt.show()

# # wykres 2, rozkład ocen
# if 'ocena' in df.columns:
#     plt.figure(figsize=(5, 7))
#     plt.plot()
#     df['ocena'].hist (bins=5, color='lightgreen', edgecolor='white')
#     plt.title('Rozklad ocen')
#     plt.xlabel('ocena')
#     plt.ylabel('Liczba ocen')
#
#     plt.show()

# Wykres 3: Zależność między alkoholem a oceną - wersja prostsza scatter

#
# plt.scatter(df['alkohol'], df['ocena'])
#
# plt.xlabel('Zawartość alko w (%)')
# plt.ylabel('ocena')
# plt.title('Zależność między zawartością alkoholu a oceną')
#
# plt.show()

# Wykres 3: Zależność między alkoholem a oceną - wersja bardziej złożona z linią trendu
#
# if 'alkohol' in df.columns and 'ocena' in df.columns:
#     plt.figure(figsize=(5, 7))
#     plt.scatter(df['alkohol'], df['ocena'], alpha=0.6, s=60, color='purple')
#     plt.title('Zależność między zawartością alkoholu a oceną')
#     plt.xlabel('Zawartość alko w (%)')
#     plt.ylabel('Ocena')
#     plt.grid(True, alpha=0.3)
#     # linia trendu
#     z = np.polyfit(df['alkohol'], df['ocena'], 1)
#     p = np.poly1d(z)
#     plt.plot(df['alkohol'], p(df['alkohol']), "r--", alpha=0.8)


# plt.show()

# Wykres 4: Popularność stylów piw
# if 'styl' in df.columns:
#     plt.figure(figsize=(10, 6))
#     df['styl'].value_counts().plot(kind='bar', color='orange', edgecolor='black')
#     plt.xlabel('Styl piwa')
#     plt.ylabel('Liczba piw')
#     plt.xticks(rotation=45)
#     plt.grid(axis='y', alpha=0.3)
#     plt.tight_layout()
#     plt.show()

    # Wykres 5: Macierz korelacji (jeśli są przynajmniej 2 kolumny numeryczne)
if len(kolumny_numeryczne) >= 2 and False: # Warunek 'False' oznacza tutaj np. 1=2, czyli jest zawsze nie spełniony, chodzi o to, żeby te wykresy nie odpalały się za każdym razem.
    plt.figure(figsize=(8, 6))
    macierz_korelacji = df[kolumny_numeryczne].corr()
    sns.heatmap(macierz_korelacji, annot=True, cmap='coolwarm')
    plt.title('Korelacje między cechami numerycznymi')
    plt.tight_layout()
    plt.show()

print("\n" "="*50)
print("POSUMOWANIE ANALIZY")
print("="*50)
print("Analiza EDA zakończona pomyślnie")
print(f"Przeanalizowano {len(df)} piw")
print(f"Liczba cech: {len(df.columns)}")

if len(kolumny_numeryczne) > 0:
    print("Znalezione cechy kategoryczne:", list(kolumny_tekstowe))

# najlepiej ocenione
if 'ocena' in df.columns and 'nazwa' in df.columns:
    print("\n3najwyżej oceniane piwa")
    najlepsze = df.nlargest(3, 'ocena')[['nazwa', 'ocena']]
    print(najlepsze)

# najwyższa zawartość alko
if 'alkohol' in df.columns and 'nazwa' in df.columns:
    print("\n3 najmocniejsze piwa")
    mocne = df.nlargest(3, 'alkohol')[['nazwa', 'alkohol']]
    print(mocne)