import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("antalya_kiralik_ev.csv")
df.info()
print(df)
print(df.describe().T)

# 1. Mahalle sayım grafiği
plt.figure(figsize=(14, 8))
mahalle_counts = df['mahalle'].value_counts()
print(mahalle_counts)
sns.barplot(x=mahalle_counts.index, y=mahalle_counts.values, palette="viridis")
plt.title("Mahalle Dağılımı")
plt.xlabel("Mahalleler")
plt.ylabel("Kiralık Ev Sayısı")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Fiyat dağılımı için histogram
plt.figure(figsize=(12, 6))
sns.histplot(df['fiyat'], bins=30, kde=True, color='skyblue')
plt.title("Kiralık Ev Fiyat Dağılımı")
plt.xlabel("Fiyat")
plt.ylabel("Frekans")
plt.tight_layout()
plt.show()

# Oda sayısını sayısal formata dönüştürme
df['oda_sayisi'] = df['oda_sayisi'].astype(str)

# 3. Oda sayısına göre kiralık ev sayıları
plt.figure(figsize=(12, 6))
sns.countplot(x='oda_sayisi', data=df, palette="viridis")
plt.title("Oda Sayısına Göre Kiralık Ev Sayıları")
plt.xlabel("Oda Sayısı")
plt.ylabel("Sayım")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Bina yaşı için sayım grafiği
plt.figure(figsize=(12, 6))
sns.countplot(x='bina_yas', data=df, palette="viridis")
plt.title("Bina Yaşına Göre Kiralık Ev Sayıları")
plt.xlabel("Bina Yaşı")
plt.ylabel("Sayım")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Dairenin bulunduğu kat için sayım grafiği
plt.figure(figsize=(12, 6))
sns.countplot(x='dairenin_bulundugu_kat', data=df, palette="viridis")
plt.title("Dairenin Bulunduğu Kat Dağılımı")
plt.xlabel("Dairenin Bulunduğu Kat")
plt.ylabel("Sayım")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Bina kat sayısı için sayım grafiği
plt.figure(figsize=(12, 6))
sns.countplot(x='bina_kat_sayisi', data=df, palette="viridis")
plt.title("Bina Kat Sayısına Göre Kiralık Ev Sayıları")
plt.xlabel("Bina Kat Sayısı")
plt.ylabel("Sayım")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Isıtma türü için sayım grafiği
plt.figure(figsize=(12, 6))
sns.countplot(x='isitma_turu', data=df, palette="viridis")
plt.title("Isıtma Türüne Göre Kiralık Ev Sayıları")
plt.xlabel("Isıtma Türü")
plt.ylabel("Sayım")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 8. Banyo sayısı için sayım grafiği
plt.figure(figsize=(12, 6))
sns.countplot(x='banyo_sayisi', data=df, palette="viridis")
plt.title("Banyo Sayısına Göre Kiralık Ev Sayıları")
plt.xlabel("Banyo Sayısı")
plt.ylabel("Sayım")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 9. Otopark durumu için sayım grafiği
plt.figure(figsize=(12, 6))
sns.countplot(x='otopark', data=df, palette="viridis")
plt.title("Otopark Durumu")
plt.xlabel("Otopark Var mı?")
plt.ylabel("Sayım")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 10. Eşya durumu için sayım grafiği
plt.figure(figsize=(12, 6))
sns.countplot(x='esya_durumu', data=df, palette="viridis")
plt.title("Eşya Durumuna Göre Kiralık Ev Sayıları")
plt.xlabel("Eşya Durumu")
plt.ylabel("Sayım")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 11. Site içinde olma durumu için sayım grafiği
plt.figure(figsize=(12, 6))
sns.countplot(x='site_icinde', data=df, palette="viridis")
plt.title("Site İçinde Olma Durumu")
plt.xlabel("Site İçinde Mi?")
plt.ylabel("Sayım")
plt.xticks(ticks=[0, 1], labels=['Hayır', 'Evet'])
plt.tight_layout()
plt.show()

# 12. Asansör durumu için sayım grafiği
plt.figure(figsize=(12, 6))
sns.countplot(x='asansor', data=df, palette="viridis")
plt.title("Asansör Durumu")
plt.xlabel("Asansör Var mı?")
plt.ylabel("Sayım")
plt.xticks(ticks=[0, 1], labels=['Yok', 'Var'])
plt.tight_layout()
plt.show()

# 13. Balkon varlığı için sayım grafiği
plt.figure(figsize=(12, 6))
sns.countplot(x='balkon', data=df, palette="viridis")
plt.title("Balkon Var mı?")
plt.xlabel("Balkon Var mı?")
plt.ylabel("Sayım")
plt.xticks(ticks=[0, 1], labels=['Yok', 'Var'])
plt.tight_layout()
plt.show()

# 14. Aylık aidat için sayım grafiği
plt.figure(figsize=(12, 6))
sns.histplot(df['aidat'], bins=30, kde=True)
plt.title("Aylık Aidat Dağılımı")
plt.xlabel("Aidat")
plt.ylabel("Frekans")
plt.tight_layout()
plt.show()

# 15. Depozito için sayım grafiği
plt.figure(figsize=(12, 6))
sns.histplot(df['depozito'], bins=30, kde=True)
plt.title("Depozito Dağılımı")
plt.xlabel("Depozito")
plt.ylabel("Frekans")
plt.tight_layout()
plt.show()

print(df.head())