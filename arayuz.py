from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import Tk, messagebox
from tkinter import Canvas
from tkinter import ttk
import joblib
import pandas as pd
import numpy as np

df_4 = pd.read_csv(r"etiketli.csv")
df = df_4.copy()

X = df.drop(["fiyat"], axis = 1)
y = df["fiyat"]

# Modeli yükleme
try:
    model = joblib.load("voting_regressor_model.pkl")
except FileNotFoundError:
    messagebox.showerror("Hata", "Model dosyası bulunamadı. Lütfen modeli kaydettiğinizden emin olun.")
    exit()
pencere = Tk()
pencere.title("Ev Fiyat Tahmini")

pencere.configure(background='#96b87b')
pencere.geometry("1400x1400")
pencere.state("normal")

def mesaj():
    messagebox.showinfo(title="Başarılı", message="Seçim başarılı")

def olumsuz():
    messagebox.showwarning(title="Dikkat", message="Seçim Yapmadınız")

# DEĞİŞKENLER

def mahalle_düzenle():
    global mahalle 
    mahalle_deger = mahalle_kutu.get()
    
    if mahalle_deger == "Bayındır Mh.":
        mahalle = 0
        mesaj()
    elif mahalle_deger == "Çaybaşı Mh.":
        mahalle = 1
        mesaj()
    elif mahalle_deger == "Güzeloba Mh.":
        mahalle = 2
        mesaj()
    elif mahalle_deger == "Şirinyalı Mh.":
        mahalle = 3
        mesaj()
    elif mahalle_deger == "Çağlayan Mh.":
        mahalle = 4
        mesaj()
    elif mahalle_deger == "Kızılsaray Mh.":
        mahalle = 5
        mesaj()
    elif mahalle_deger == "Zerdalilik Mah.":
        mahalle = 6
        mesaj()
    elif mahalle_deger == "Kızılarık Mh.":
        mahalle = 7
        mesaj()
    elif mahalle_deger == "Meydankavağı Mh.":
        mahalle = 8
        mesaj()
    elif mahalle_deger == "Yenigün Mh.":
        mahalle = 9
        mesaj()
    elif mahalle_deger == "Meltem Mah.":
        mahalle = 10
        mesaj()
    elif mahalle_deger == "Elmalı Mh.":
        mahalle = 11
        mesaj()
    elif mahalle_deger == "Güvenlik Mh.":
        mahalle = 12
        mesaj()
    elif mahalle_deger == "Gebizli Mah.":
        mahalle = 13
        mesaj()
    elif mahalle_deger == "Muratpaşa Mh.":
        mahalle = 14
        mesaj()
    elif mahalle_deger == "Etiler Mah.":
        mahalle = 15
        mesaj()
    elif mahalle_deger == "Fener Mah.":
        mahalle = 16
        mesaj()
    elif mahalle_deger == "Yüksekalan Mh.":
        mahalle = 17
        mesaj()
    elif mahalle_deger == "Varlık Mh.":
        mahalle = 18
        mesaj()
    elif mahalle_deger == "Konuksever Mah.":
        mahalle = 19
        mesaj()
    elif mahalle_deger == "Doğuyaka Mh.":
        mahalle = 20
        mesaj()
    elif mahalle_deger == "Haşimişcan Mh.":
        mahalle = 21
        mesaj()
    elif mahalle_deger == "Gençlik Mh.":
        mahalle = 22
        mesaj()
    elif mahalle_deger == "Yeşilbahçe Mh.":
        mahalle = 23
        mesaj()
    elif mahalle_deger == "Sedir Mah.":
        mahalle = 24
        mesaj()
    elif mahalle_deger == "Sinan Mah.":
        mahalle = 25
        mesaj()
    elif mahalle_deger == "Deniz Mah.":
        mahalle = 26
        mesaj()
    elif mahalle_deger == "Altındağ Mh.":
        mahalle = 27
        mesaj()
    elif mahalle_deger == "Dutlubahçe Mh.":
        mahalle = 28
        mesaj()
    elif mahalle_deger == "Bahçelievler Mh.":
        mahalle = 29
        mesaj()
    elif mahalle_deger == "Üçgen Mh.":
        mahalle = 30
        mesaj()
    elif mahalle_deger == "Mehmetçik Mh.":
        mahalle = 31
        mesaj()
    elif mahalle_deger == "Kışla Mh.":
        mahalle = 32
        mesaj()
    elif mahalle_deger == "Güzelbağ Mh.":
        mahalle = 33
        mesaj()
    elif mahalle_deger == "Cumhuriyet Mah.":
        mahalle = 34
        mesaj()
    elif mahalle_deger == "Kızıltoprak Mh.":
        mahalle = 35
        mesaj()
    elif mahalle_deger == "Güzeloluk Mh.":
        mahalle = 36
        mesaj()
    elif mahalle_deger == "Soğuksu Mh.":
        mahalle = 37
        mesaj()
    elif mahalle_deger == "Demircikara Mah.":
        mahalle = 38
        mesaj()
    elif mahalle_deger == "Tahılpazarı Mh.":
        mahalle = 39
        mesaj()
    elif mahalle_deger == "Yıldız Mh.":
        mahalle = 40
        mesaj()
    elif mahalle_deger == "Yeşildere Mh.":
        mahalle = 41
        mesaj()
    elif mahalle_deger == "Ermenek Mah.":
        mahalle = 42
        mesaj()
    elif mahalle_deger == "Balbey Mah.":
        mahalle = 43
        mesaj()
    elif mahalle_deger == "Yenigöl Mh.":
        mahalle = 44
        mesaj()
    elif mahalle_deger == "Selçuk Mh.":
        mahalle = 45
        mesaj()
    elif mahalle_deger == "Topçular Mh.":
        mahalle = 46
        mesaj()
    elif mahalle_deger == "Memurevleri Mah.":
        mahalle = 47
        mesaj()
    elif mahalle_deger == "Kırcami Mh.":
        mahalle = 48
        mesaj()
    elif mahalle_deger == "Yeşilova Mh.":
        mahalle = 49
        mesaj()
    else:
        olumsuz()
    
    print(mahalle)

def brut_alan_düzenle():
    global brut
    brut_alan_m2 = int(alan_entry.get())
    
    # Brut alanı 0'dan büyükse
    if brut_alan_m2 > 0:
        brut = brut_alan_m2
        mesaj()  # Eğer değer geçerliyse mesaj fonksiyonu çalışır
        print(f"Brut Alan (m2): {brut_alan_m2}")
    else:
        olumsuz()  # Eğer değer geçersizse olumsuz fonksiyonu çalışır


def net_düzenle():
    global net
    net_alan_m2 = int(net_entry.get())
    if(net_alan_m2 > 0):
        net = net_alan_m2
        mesaj()
        print(net_alan_m2)
    else:
        olumsuz()
    
    
def oda_düzenle():
    global oda
    oda_deger = oda_kutu.get()

    if oda_deger == "2+1":
        oda = 1
        mesaj()
    elif oda_deger == "3+1":
        oda = 2
        mesaj()
    elif oda_deger == "4+2":
        oda = 3
        mesaj()
    elif oda_deger == "1+1":
        oda = 4
        mesaj()
    elif oda_deger == "Stüdyo (1+0)":
        oda = 5
        mesaj()
    elif oda_deger == "4+1":
        oda = 6
        mesaj()
    elif oda_deger == "5+1":
        oda = 7
        mesaj()
    elif oda_deger == "2.5+1":
        oda = 8
        mesaj()
    elif oda_deger == "6+1":
        oda = 9
        mesaj()
    elif oda_deger == "2+0":
        oda = 10
        mesaj()
    elif oda_deger == "5+2":
        oda = 11
        mesaj()
    elif oda_deger == "3.5+1":
        oda = 12
        mesaj()
    else:
        olumsuz()
    
def yaş_düzenle():
    global yaş
    yaş_deger = yaşlar_kutu.get()
    
    # Bina yaşı değerlerine göre eşleştirmeler
    if yaş_deger == "21-25 arası":
        yaş = 1
        mesaj()
    elif yaş_deger == "0":
        yaş = 2
        mesaj()
    elif yaş_deger == "11-15 arası":
        yaş = 3
        mesaj()
    elif yaş_deger == "5-10 arası":
        yaş = 4
        mesaj()
    elif yaş_deger == "16-20 arası":
        yaş = 5
        mesaj()
    elif yaş_deger == "26-30 arası":
        yaş = 6
        mesaj()
    elif yaş_deger == "31 ve üzeri":
        yaş = 7
        mesaj()
    elif yaş_deger == "1":
        yaş = 8
        mesaj()
    elif yaş_deger == "4":
        yaş = 9
        mesaj()
    elif yaş_deger == "3":
        yaş = 10
        mesaj()
    elif yaş_deger == "2":
        yaş = 11
        mesaj()
    else:
        olumsuz()
        
def site_düzenle():
    global site
    site_deger = site_kutu.get()
    
    # Site durumu kontrolü
    if site_deger == "Evet":  # "Evet" durumu
        site = 0
        mesaj()
    elif site_deger == "Hayır":  # "Hayır" durumu
        site = 1
        mesaj()
    else:
        olumsuz()
    
def eşya_düzenle():
    global eşya
    eşya_deger = eşya_kutu.get()
    
    # Eşya durumu kontrolü
    if eşya_deger == "Eşyalı":  # "Eşyalı" durumu
        eşya = 1
        mesaj()
    elif eşya_deger == "Boş":  # "Boş" durumu
        eşya = 0
        mesaj()
    else:
        olumsuz()

def ısıtma_düzenle():
    global ısıtma
    ısıtma_deger = ısıtma_kutu.get()
    
    if ısıtma_deger == "Klima":
        ısıtma = 0
        mesaj()
    elif ısıtma_deger == "Kombi (Doğalgaz)":
        ısıtma = 1
        mesaj()
    elif ısıtma_deger == "Doğalgaz Sobası":
        ısıtma = 2
        mesaj()
    elif ısıtma_deger == "Yerden Isıtma":
        ısıtma = 3
        mesaj()
    elif ısıtma_deger == "Yok":
        ısıtma = 4
        mesaj()
    elif ısıtma_deger == "Kombi (Elektrik)":
        ısıtma = 5
        mesaj()
    elif ısıtma_deger == "Soba":
        ısıtma = 6
        mesaj()
    elif ısıtma_deger == "Merkezi (Pay Ölçer)":
        ısıtma = 7
        mesaj()
    elif ısıtma_deger == "Şömine":
        ısıtma = 8
        mesaj()
    elif ısıtma_deger == "Kat Kaloriferi":
        ısıtma = 9
        mesaj()
    elif ısıtma_deger == "Fancoil Ünitesi":
        ısıtma = 10
        mesaj()
    elif ısıtma_deger == "Güneş Enerjisi":
        ısıtma = 11
        mesaj()
    elif ısıtma_deger == "Merkezi":
        ısıtma = 12
        mesaj()
    else:
        olumsuz()

    
def banyo_düzenle():
    global banyo
    banyo_deger = banyo_kutu.get()
    if(banyo_deger == "0"):
        banyo = 0
        mesaj()
    elif(banyo_deger == "1"):
        banyo = 1
        mesaj()
    elif(banyo_deger == "2"):
        banyo = 2
        mesaj()
    elif(banyo_deger == "3"):
        banyo = 3
        mesaj()
    elif(banyo_deger == "4"):
        banyo = 4
        mesaj()
    elif(banyo_deger == "5"):
        banyo = 5
        mesaj()
    elif(banyo_deger == "6+"):
        banyo = 6
        mesaj()
    else:
        olumsuz()
def daire_düzenle():
    global daire
    daire_deger = daire_kutu.get()
    
    if daire_deger == "Giriş Katı":
        daire = 0
        mesaj()
    elif daire_deger == "1":
        daire = 1
        mesaj()
    elif daire_deger == "2":
        daire = 2
        mesaj()
    elif daire_deger == "3":
        daire = 3
        mesaj()
    elif daire_deger == "4":
        daire = 4
        mesaj()
    elif daire_deger == "5":
        daire = 5
        mesaj()
    elif daire_deger == "6":
        daire = 6
        mesaj()
    elif daire_deger == "7":
        daire = 7
        mesaj()
    elif daire_deger == "8":
        daire = 8
        mesaj()
    elif daire_deger == "9":
        daire = 9
        mesaj()
    elif daire_deger == "10":
        daire = 10
        mesaj()
    elif daire_deger == "Villa Tipi":
        daire = 11
        mesaj()
    elif daire_deger == "Çatı Katı":
        daire = 12
        mesaj()
    elif daire_deger == "Bahçe Katı":
        daire = 13
        mesaj()
    elif daire_deger == "Bodrum Kat":
        daire = 14
        mesaj()
    else:
        olumsuz()

def kat_düzenle():
    global bina_kat_sayisi
    kat_deger = kat_kutu.get()
    
    # Bina kat sayısını kontrol et
    if kat_deger.isdigit():  # Eğer sayısal bir değer girildiyse
        kat_deger = int(kat_deger)
        if kat_deger in [4, 5, 3, 8, 10, 9, 11, 2, 7, 15, 13, 6, 14, 12, 1, 16, 17]:  # Geçerli kat sayısı
            bina_kat_sayisi = kat_deger
            mesaj()
        else:
            olumsuz()  # Geçersiz kat sayısı
    else:
        olumsuz()

def asansor_düzenle():
    global asansor
    asansor_deger = asansor_kutu.get()
    
    # Asansör durumu kontrolü
    if asansor_deger == "Var":  # "Var" durumu
        asansor = 1
        mesaj()
    elif asansor_deger == "Yok":  # "Yok" durumu
        asansor = 0
        mesaj()
    else:
        olumsuz()

def balkon_düzenle():
    global balkon
    balkon_deger = balkon_kutu.get()
    
    # Balkon durumu kontrolü
    if balkon_deger == "Var":  # "Var" durumu
        balkon = 1
        mesaj()
    elif balkon_deger == "Yok":  # "Yok" durumu
        balkon = 0
        mesaj()
    else:
        olumsuz()

def otopark_düzenle():
    global otopark
    otopark_deger = otopark_kutu.get()
    
    # Otopark durumu kontrolü
    if otopark_deger == "Açık Otopark":  # "Açık Otopark" durumu
        otopark = 1
        mesaj()
    elif otopark_deger == "Kapalı Otopark":  # "Kapalı Otopark" durumu
        otopark = 2
        mesaj()
    elif otopark_deger == "Yok":  # "Yok" durumu
        otopark = 0
        mesaj()
    elif otopark_deger == "Açık & Kapalı Otopark":  # "Açık & Kapalı Otopark" durumu
        otopark = 3
        mesaj()
    else:
        olumsuz()

def aidat_düzenle():
    global aidat
    aidat_deger = aidat_entry.get()
    
    # Aidat kontrolü (sayı olup olmadığını kontrol et)
    if aidat_deger.isdigit():  # Eğer sayısal bir değer girildiyse
        aidat = int(aidat_deger)
        mesaj()
    else:
        olumsuz()

def depozito_düzenle():
    global depozito
    depozito_deger = depozito_entry.get()
    
    # Depozito kontrolü (sayı olup olmadığını kontrol et)
    if depozito_deger.isdigit():  # Eğer sayısal bir değer girildiyse
        depozito = int(depozito_deger)
        mesaj()
    else:
        olumsuz()

        
        
baslık_label = Label(pencere, text = "EV FİYAT TAHMİNİ", font="helvetica 50",borderwidth=10, padx = 320, pady = 2,
                     background = "#54941f")        
baslık_label.place(x = 70 ,y = 20)
        
        

# MAHALLE KISMI
mahalle_label = Label(text = "Mahalle Seçimi", font="helvetica 12", borderwidth=6 , padx=20)
mahalle_label.place(x = 90, y = 150)

mahalleler = ['Bayındır Mh.', 'Çaybaşı Mh.', 'Güzeloba Mh.', 'Şirinyalı Mh.',
              'Çağlayan Mh.', 'Kızılsaray Mh.', 'Zerdalilik Mah.', 'Kızılarık Mh.',
              'Meydankavağı Mh.', 'Yenigün Mh.', 'Meltem Mah.', 'Elmalı Mh.',
              'Güvenlik Mh.', 'Gebizli Mah.', 'Muratpaşa Mh.', 'Etiler Mah.',
              'Fener Mah.', 'Yüksekalan Mh.', 'Varlık Mh.', 'Konuksever Mah.',
              'Doğuyaka Mh.', 'Haşimişcan Mh.', 'Gençlik Mh.', 'Yeşilbahçe Mh.',
              'Sedir Mah.', 'Sinan Mah.', 'Deniz Mah.', 'Altındağ Mh.', 'Dutlubahçe Mh.',
              'Bahçelievler Mh.', 'Üçgen Mh.', 'Mehmetçik Mh.', 'Kışla Mh.', 'Güzelbağ Mh.',
              'Cumhuriyet Mah.', 'Kızıltoprak Mh.', 'Güzeloluk Mh.', 'Soğuksu Mh.',
              'Demircikara Mah.', 'Tahılpazarı Mh.', 'Yıldız Mh.', 'Yeşildere Mh.',
              'Ermenek Mah.', 'Balbey Mah.', 'Yenigöl Mh.', 'Selçuk Mh.', 'Topçular Mh.',
              'Memurevleri Mah.', 'Kırcami Mh.', 'Yeşilova Mh.']
mahalle_kutu = Combobox(pencere, values = mahalleler)
mahalle_kutu.place(x = 90, y = 200)

mahalle_buton = Button(pencere, text = "Seç", command = mahalle_düzenle, font="helvetica 12", borderwidth=6, padx=40)
mahalle_buton.place(x = 90, y = 250)

# BRÜT ALAN DÜZENLE
alan_label = Label(pencere, text = "Brüt Alanını Girin", font="helvetica 12",borderwidth=6)
alan_label.place(x = 290, y = 150)

alan_entry = Entry()
alan_entry.place(x = 290, y = 200)

alan_buton = Button(pencere, text = "Seç", command = brut_alan_düzenle, font="helvetica 12",borderwidth=6, padx=40)
alan_buton.place(x = 290, y = 250)

# NET METREKARE
net_label = Label(text = "Net Metrekareyi Giriniz", font="helvetica 12",borderwidth=6)
net_label.place(x = 490, y = 150)

net_entry = Entry()
net_entry.place(x = 490, y = 200)

net_buton = Button(pencere, text = "Seç", command = net_düzenle, font="helvetica 12",borderwidth=6, padx=40)
net_buton.place(x = 490, y = 250)

# BİNA KAT SAYISI
kat_label = Label(text = "Bina Kat Sayısı", font="helvetica 12",borderwidth=6 , padx=20)
kat_label.place(x = 690, y = 150)
katlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

kat_kutu = Combobox(pencere, values = katlar)
kat_kutu.place(x = 690, y = 200)

kat_buton = Button(pencere, text = "Seç", command = kat_düzenle, font="helvetica 12",borderwidth=6, padx=40)
kat_buton.place(x = 690, y = 250)

# DAİRENİN KATI
daire_label = Label(text = "Daire Katı", font="helvetica 12",borderwidth=6 , padx=40)
daire_label.place(x = 890, y = 150)

# Veritabanındaki daire katlarına uygun seçenekler
daireler = ["Giriş Katı", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10-20", 
            "20-30", "30-40", "Bahçe Katı", "Bodrum Katı", "Çatı Katı", "Villa Tipi", 
            "Çatı Dublex", "Bahçe Dublex", "Müstakil", "Zemin Kat", "Yüksek Giriş", 
            "Giriş Altı Kot 2", "11", "12", "13", "15"]

daire_kutu = Combobox(pencere, values = daireler)
daire_kutu.place(x = 890, y = 200)

daire_buton = Button(pencere, text = "Seç", command = daire_düzenle, font="helvetica 12",borderwidth=6, padx= 40)
daire_buton.place(x = 890, y = 250)

# BİNA YAŞI
yaş_label = Label(text = "Bina Yaşı", font="helvetica 12",borderwidth=6 , padx=40)
yaş_label.place(x = 1090, y = 150)
yaşlar = ["0", "1", "2", "3", "4", "5-10", "11-15", "16-20", "21-25", "26-30", "31 ve üzeri"]
yaşlar_kutu = Combobox(pencere, values = yaşlar)
yaşlar_kutu.place(x = 1090, y = 200)

yaşlar_buton = Button(pencere, text = "Seç", command = yaş_düzenle, font="helvetica 12",borderwidth=6, padx= 40)
yaşlar_buton.place(x = 1090, y = 250)

#---------------------------2.sıra---------------------------------

# ODA SAYISI
oda_label = Label(text = "Oda Sayısı Seçiniz", font="helvetica 12", borderwidth=6)
oda_label.place(x = 90, y = 350)

# Oda sayısı seçenekleri
odalar = ["1+1", "2+0", "2+1", "2.5+1", "3+1", "3.5+1", "4+1", "4+2", "5+1", "5+2", "6+1", "Stüdyo (1+0)"]
oda_kutu = Combobox(pencere, values = odalar)
oda_kutu.place(x = 90, y = 400)

oda_buton = Button(pencere, text = "Seç", command = oda_düzenle, font="helvetica 12", borderwidth=6, padx= 40)
oda_buton.place(x = 90, y = 450)

# BANYO SAYISI
banyo_label = Label(text = "Banyo Sayısı", font="helvetica 12",borderwidth=6)
banyo_label.place(x = 290, y = 350)

banyolar  = ["0","1","2","3","4","5","6+"]
banyo_kutu = Combobox(pencere, values = banyolar)
banyo_kutu.place(x = 290, y = 400)

banyo_buton = Button(pencere, text = "Seç", command = banyo_düzenle, font="helvetica 12",borderwidth=6, padx= 40)
banyo_buton.place(x = 290, y = 450)

# ISITMA
ısıtma_label = Label(text = "Isıtma Türünü Seçiniz", font="helvetica 12",borderwidth=6)
ısıtma_label.place(x = 490, y = 350)

# Veritabanındaki ısıtma türlerine göre seçenekler
ısıtmalar = ["Klima", "Kombi (Doğalgaz)", "Doğalgaz Sobası", "Yerden Isıtma", "Yok", 
             "Kombi (Elektrik)", "Soba", "Merkezi (Pay Ölçer)", "Şömine", 
             "Kat Kaloriferi", "Fancoil Ünitesi", "Güneş Enerjisi", "Merkezi"]
ısıtma_kutu = Combobox(pencere, values = ısıtmalar)
ısıtma_kutu.place(x = 490, y = 400)

ısıtma_buton = Button(pencere, text = "Seç", command = ısıtma_düzenle, font="helvetica 12",borderwidth=6, padx= 40)
ısıtma_buton.place(x = 490, y = 450)

# BALKON
balkon_label = Label(text = "Balkon", font="helvetica 12",borderwidth=6 , padx=40)
balkon_label.place(x = 690, y = 350)

balkon_kutu = Combobox(pencere, values = ["Var", "Yok"])
balkon_kutu.place(x = 690, y = 400)

balkon_buton = Button(pencere, text = "Seç", command = balkon_düzenle, font="helvetica 12",borderwidth=6 , padx=40)
balkon_buton.place(x = 690, y = 450)

#EŞYA DURUMU
eşya_label = Label(pencere, text = "Eşya Durumu", font="helvetica 12",borderwidth=6)
eşya_label.place(x = 890, y = 350)

eşyalar = ["Boş","Eşyalı"]
eşya_kutu = Combobox(pencere, values = eşyalar)
eşya_kutu.place(x = 890, y = 400)

eşya_buton = Button(pencere, text = "Seç", command = eşya_düzenle, font="helvetica 12",borderwidth=6, padx= 40)
eşya_buton.place(x = 890, y = 450)
#------------------------3.Sıra --------

# SİTE İÇERİSİNDE
site_label = Label(text = "Site İçerisinde mi?", font="helvetica 12",borderwidth=6)
site_label.place(x = 90, y = 550)
siteler = ["Evet","Hayır"]
site_kutu = Combobox(pencere, values = siteler)
site_kutu.place(x = 90, y = 600)

site_buton = Button(pencere, text = "Seç", command = site_düzenle, font="helvetica 12",borderwidth=6, padx= 40)
site_buton.place(x = 90, y = 650)

# ASANSÖR
asansor_label = Label(text = "Asansör", font="helvetica 12",borderwidth=6 , padx=40)
asansor_label.place(x = 290, y = 550)

asansor_kutu = Combobox(pencere, values = ["Var", "Yok"])
asansor_kutu.place(x = 290, y = 600)

asansor_buton = Button(pencere, text = "Seç", command = asansor_düzenle, font="helvetica 12",borderwidth=6, padx= 40)
asansor_buton.place(x = 290, y = 650)

# OTOPARK
otopark_label = Label(text = "Otopark", font="helvetica 12",borderwidth=6 , padx=40)
otopark_label.place(x = 490, y = 550)

otoparklar = ["Açık Otopark", "Kapalı Otopark", "Yok", "Açık & Kapalı Otopark"]
otopark_kutu = Combobox(pencere, values = otoparklar)
otopark_kutu.place(x = 490, y = 600)

otopark_buton = Button(pencere, text = "Seç", command = otopark_düzenle, font="helvetica 12",borderwidth=6, padx= 40)
otopark_buton.place(x = 490, y = 650)

# AİDAT
aidat_label = Label(text = "Aidat Miktarını Giriniz", font="helvetica 12",borderwidth=6)
aidat_label.place(x = 690, y = 550)

aidat_entry = Entry()
aidat_entry.place(x = 690, y = 600)

aidat_buton = Button(pencere, text = "Seç", command = aidat_düzenle, font="helvetica 12",borderwidth=6, padx= 40)
aidat_buton.place(x = 690, y = 650)

# DEPOZİTO
depozito_label = Label(text = "Depozito Miktarını Giriniz", font="helvetica 12",borderwidth=6)
depozito_label.place(x = 890, y = 550)

depozito_entry = Entry()
depozito_entry.place(x = 890, y = 600)

depozito_buton = Button(pencere, text = "Seç", command = depozito_düzenle, font="helvetica 12",borderwidth=6, padx= 40)
depozito_buton.place(x = 890, y = 650)

# ML KISIM BAŞLANGIÇ

def hesapla():
    yeni_veri = [[mahalle], [brut], [net], [oda], [bina_kat_sayisi],[daire], [yaş], [ısıtma], [banyo], [balkon], [asansor], [otopark], [eşya], [site], [aidat], [depozito]]
    # DataFrame'e dönüştürme
    yeni_veri = pd.DataFrame(yeni_veri).T

    # Yeni veri kümesini sütun başlıklarıyla eşleştiriyoruz
    df_2 = yeni_veri.rename(columns={
        0: "mahalle",
        1: "brut_alan_m2",
        2: "net_alan_m2",
        3: "oda_sayisi",
        4: "bina_kat_sayisi",
        5: "dairenin_bulundugu_kat",
        6: "bina_yas",
        7: "isitma_turu",
        8: "banyo_sayisi",
        9: "balkon",
        10: "asansor",
        11: "otopark",
        12: "esya_durumu",
        13: "site_icinde",
        14: "aidat",
        15: "depozito"
    })

    # Yeni düzenlenmiş veri
    print(df_2)

    
    prediction = model.predict(df_2)   
    if(prediction < 0):
        prediction = -1*prediction
    
    prediction = int(prediction)
    
    s2 = Label(pencere, text = prediction, font="helvetica 20",borderwidth=6, padx = 45, pady = 20,background = "#cdf0b1")
    s2.place(x = 1100, y = 450)
    
    
# HESAPLA
hesapla_buton = Button(pencere, text = "HESAPLA", command = hesapla, font="helvetica 15",borderwidth=10, padx = 40, pady = 20, background = "#cdf0b1")
hesapla_buton.place(x = 1100, y = 350)

s1 = Label(pencere, text= "Tahmini Kira Fiyatı", font="helvetica 12",borderwidth=6, padx = 30, pady = 20 ,background = "#cdf0b1")
s1.place(x = 1100, y = 450)

mainloop()