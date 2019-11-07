import matplotlib.dates as mdt
import pandas as pd
from datetime import date
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.techindicators import TechIndicators

cc = CryptoCurrencies(key='uwu', output_format='json')
ti = TechIndicators(key='owo', output_format='json')
class Coins:
    def __init__(self, crypto, base_currency, periodo):
        
        self.crypto = crypto
        self.base_currency = base_currency
        self.periodo = periodo

    def send_Crypto(self):
        

        dados, metadados = cc.get_digital_currency_daily(symbol=self.crypto, market=self.base_currency)
        datas = []
        if self.periodo == 0:
            datas = [index for index, value in dados.items()]

        else:
            count = 0
            for index, value in dados.items():
                datas.append(index)
                count += 1
                if count > self.periodo:
                    break
                    
        open_Info = [int(float(dados[data]["1a. open ({})".format(self.base_currency)])) for data in datas]
        high_Info = [int(float(dados[data]["2a. high ({})".format(self.base_currency)])) for data in datas]
        low_Info = [int(float(dados[data]["3a. low ({})".format(self.base_currency)])) for data in datas]
        close_Info = [int(float(dados[data]["4a. close ({})".format(self.base_currency)])) for data in datas]
        volume_Info = [int(float(dados[data]["5. volume"])) for data in datas]
        #cap_Info = [int(float(dados[data]["6. market cap (USD)".format(self.crypto)])) for data in datas]

        return {
            "time" : [mdt.date2num(date(int(data[0:4]), int(data[5:7]), int(data[8:10]))) for data in datas],
            "datetime": datas,
            "open": open_Info,
            "high": high_Info,
            "low": low_Info,
            "close": close_Info,
            "volume": volume_Info,
            #"cap": cat_Info
        
        
        }

    def send_SMA(self):

        dados, meta_dados = ti.get_sma(symbol=self.crypto+self.base_currency, interval='daily', time_period=30, series_type=open)
        
        datas = []
        if self.periodo == 0:
            datas = [index for index, value in dados.items()]

        else:
            count = 0
            for index, value in dados.items():
                datas.append(index)
                count += 1
                if count > self.periodo:
                    break
        
        moving_Average = [int(float(dados[data]["SMA"])) for data in datas]

        return {
            "datas": [mdt.date2num(date(int(data[0:4]), int(data[5:7]), int(data[8:10]))) for data in datas],
            "media": moving_Average
        }