import pandas as pd
from sklearn import preprocessing #etiketleme için

df = pd.read_csv("antalya_kiralik_ev.csv")
#df.drop("Unnamed: 0", axis = 1, inplace = True)
#print(df.columns)

#Sütun düzenleme
df_2 = df[['mahalle', 'brut_alan_m2', 'net_alan_m2', 'oda_sayisi', 
           'bina_kat_sayisi', 'dairenin_bulundugu_kat', 'bina_yas', 
           'isitma_turu', 'banyo_sayisi', 'balkon', 'asansor', 
           'otopark', 'esya_durumu', 'site_icinde', 'sahibi','aidat', 'depozito', 'fiyat']]

print(df_2.head())
print(df_2.columns)
#df_2.to_csv("antalya_kiralik_ev.csv", index=False)

#Etiketleme
df = pd.read_csv("antalya_kiralik_ev.csv")
print(df.head())
df_2 = df.copy()
df_3 = df.copy()

le = preprocessing.LabelEncoder()

"""
df_3["mahalle"] = le.fit_transform(df_2.mahalle) #Etiketleme
print(le.classes_) # etiketlenen veriler
print(df_3.mahalle.unique()) #etiket sayıları
print(le.inverse_transform([1])) #etiketli veri
"""

# Kategorik sütunlar
categorical_columns = ['mahalle', 'oda_sayisi', 'dairenin_bulundugu_kat', 'bina_yas', 'isitma_turu',
                       'balkon', 'asansor', 'otopark', 'esya_durumu', 'site_icinde', 'sahibi']

# Her bir kategorik sütun için etiketleme işlemi
for column in categorical_columns:
    # Etiketleme işlemi
    df_3[column] = le.fit_transform(df_2[column])  # Etiketleme
    print(f"Etiketlenen {column} verileri:")
    print(le.classes_)  # Etiketlenen veriler
    print(df_3[column].unique())  # Etiket sayıları
    print(le.inverse_transform([1]))  # Etiketli veri
    print("-" * 50)

df_3.to_csv("etiketli.csv" ,index=False)
etiketli = pd.read_csv("etiketli.csv")
print(etiketli.head)