import pandas as pd
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn import model_selection

df = pd.read_csv("etiketli.csv")
print(df)
print(df.columns)
#çalışılacak sutünlar (sahibi sütunu gereksiz görüldüğü için kaldırıldı)
df_2 = df.copy()

df_2 = df[['mahalle', 'brut_alan_m2', 'net_alan_m2', 'oda_sayisi', 
           'bina_kat_sayisi', 'dairenin_bulundugu_kat', 'bina_yas', 
           'isitma_turu', 'banyo_sayisi', 'balkon', 'asansor', 
           'otopark', 'esya_durumu', 'site_icinde', 'aidat', 'depozito', 'fiyat']]

print(df_2)

#bağımlı ve bağımsız değişkenler belirlendi
x = df_2.drop(['fiyat'],axis=1)
y = df_2['fiyat']
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size = 0.25,random_state = 144)
#GridSearch ile En iyi parametleri belirleme
params = {"colsample_bytree":[0.4,0.5,0.6],
         "learning_rate":[0.01,0.02,0.09],
         "max_depth":[2,3,4,5,6],
         "n_estimators":[100,200,500,2000]}
xgb = XGBRegressor()
grid = GridSearchCV(xgb, params, cv = 10, n_jobs = -1, verbose = 2)
grid.fit(x_train, y_train)
grid.best_params_
