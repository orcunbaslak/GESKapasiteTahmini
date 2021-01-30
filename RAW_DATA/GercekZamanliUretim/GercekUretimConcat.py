## for data
import pandas as pd
import numpy as np

df_1 = pd.read_csv("GercekZamanliUretim-01012018-31122018.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")
df_2 = pd.read_csv("GercekZamanliUretim-01012019-31122019.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")
df_3 = pd.read_csv("GercekZamanliUretim-01012020-31122020.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")

df_temp = [df_1, df_2, df_3]
df = pd.concat(df_temp)
df.columns = ["Date","Toplam","DogalGaz","Barajli","Linyit","Akarsu","IthalKomur","Ruzgar","Gunes","FuelOil","Jeotermal","AsfaltitKomur","TasKomur","Biyokutle","Nafta","LNG","Uluslararasi"]
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print(df.size)
print(df.dtypes)
print(df.head(20))
df.to_csv("GercekZamanliUretim-2018-2020.csv")

print("ahoy")
