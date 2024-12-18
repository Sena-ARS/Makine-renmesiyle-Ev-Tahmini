import pandas as pd

data = pd.read_csv("antalya_kiralik_ev.csv")
# Her sütundaki eşsiz değerleri döndür
unique_values = {}
for column in data.columns:
    unique_values[column] = data[column].unique()

# Sonuçları ekrana yazdır
for column, values in unique_values.items():
    print(f"Sütun: {column}")
    print(f"Farklı Değerler: {values}")
    print("-" * 40)
