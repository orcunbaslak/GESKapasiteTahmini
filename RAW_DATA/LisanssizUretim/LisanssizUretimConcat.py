## for data
import pandas as pd
import numpy as np

df_1 = pd.read_csv("lisanssizUretimMiktari-1.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")
df_2 = pd.read_csv("lisanssizUretimMiktari-2.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")
df_3 = pd.read_csv("lisanssizUretimMiktari-3.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")
df_4 = pd.read_csv("lisanssizUretimMiktari-4.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")
df_5 = pd.read_csv("lisanssizUretimMiktari-5.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")
df_6 = pd.read_csv("lisanssizUretimMiktari-6.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")
df_7 = pd.read_csv("lisanssizUretimMiktari-7.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")
df_8 = pd.read_csv("lisanssizUretimMiktari-8.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")


df_temp = [df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8]
df = pd.concat(df_temp)
df.columns = ["Date","ToplamLisanssizUretim","Ruzgar","Biyogaz","KanalTipi","Biyokutle","Gunes","Diger"]
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 26.304 adet row çıkması lazım. 2020 leap year.
print("Row:"+str(len(df.index)))
print(df.size)
print(df.dtypes)
print(df.head(20))
df.to_csv("LisanssizUretim-2018-2020.csv")

print("ahoy")
