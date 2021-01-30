## for data
import pandas as pd
import numpy as np

gercek_zamanli_tuketim_1 = pd.read_csv("GercekZamanliTuketim-01012018-31122018.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")
gercek_zamanli_tuketim_2 = pd.read_csv("GercekZamanliTuketim-01012019-31122019.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")
gercek_zamanli_tuketim_3 = pd.read_csv("GercekZamanliTuketim-01012020-31122020.csv", parse_dates=[['Tarih', 'Saat']], thousands=".", decimal=",")

df = [gercek_zamanli_tuketim_1, gercek_zamanli_tuketim_2, gercek_zamanli_tuketim_3]
gercek_zamanli_tuketim = pd.concat(df)
gercek_zamanli_tuketim.columns = ["Date", "PowerConsumption"]
gercek_zamanli_tuketim['Date'] = pd.to_datetime(gercek_zamanli_tuketim['Date'])
gercek_zamanli_tuketim.set_index('Date', inplace=True)

print(gercek_zamanli_tuketim.size)
print(gercek_zamanli_tuketim.dtypes)
print(gercek_zamanli_tuketim.head())
gercek_zamanli_tuketim.to_csv("GercekZamanliTuketim-2018-2020.csv")

print("ahoy")
