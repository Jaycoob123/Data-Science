import pandas as pd
import numpy as np

# 1 Pobrać i sprawdzić plik

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

try:

    df = pd.read_csv(url)
    print("Dane zostały pomyślnie wczytane!")
except Exception as e:
    print(f"Błąd podczas wczytywania: {e}")
    exit()



