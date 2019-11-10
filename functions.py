from alpha_vantage.cryptocurrencies import CryptoCurrencies

import matplotlib.dates as mdt
from datetime import date

import matplotlib.pyplot as plt
import mpl_finance as mpl
import numpy as np

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

datadict = [[k, []] for k in ["tempoTotal", "openTotal", "highTotal", "lowTotal", "closeTotal", "volumeTotal", "dataTotal", "nomes", "totalTime"]]

# Pede as informações das moedas pelo Wrapper do AlphaVantage e separa em dados e metados
def Request(crypto, moeda):
    cc = CryptoCurrencies(key='3DEMOuwu', output_format='json')
    data, metadata = cc.get_digital_currency_daily(symbol=crypto, market = moeda)
    return data, metadata

#Lê as informações presentes nos dados
def Read(crypto, moeda):

    request, metadados = Request(crypto, moeda)
    open = []
    high = []
    low = []
    close = []
    volume = []
    datas = []
    

    tempo = [i for i, v in request.items()]
    
    for key, value in request.items():
        open.append(float(value['1a. open ({})'.format(moeda)]))
        high.append(float(value['2a. high ({})'.format(moeda)]))
        low.append(float(value['3a. low ({})'.format(moeda)]))
        close.append(float(value['4a. close ({})'.format(moeda)]))
        volume.append(float(value['5. volume']))
    #Formação da data
    tempoCerto = [mdt.date2num(date(int(data[0:4]), int(data[5:7]), int(data[8:10]))) for data in tempo]

    #Formatação das informações do Json
    for i in [open, high, low, close, volume, tempoCerto]:
        i = i[::-1]
    for i  in [open, high, low, close]:
        [int(float(j)) for j in i]
    
    listt = [tempoCerto, open, high, low, close, volume, datas, crypto, request]
    for i in range(len(datadict)):
        datadict[i][1].append(listt[i])
        

    
#Plota o gráfico usando a lista com todas as informações
def plot(datadict):
    
    figure, axis = plt.subplots(2, 2)
    count = 0
    
    for i in range(0, 2):
        for j in range(0, 2):
            info = []
            for element in range(len(datadict[0][1][count])):
                info.append(
                    tuple 
                        ([datadict[k][1][count][element] for k in range(0, 5)]
                        ))
            mpl.candlestick_ohlc(axis[i][j], info, width=0.2, colorup='g', colordown='r', alpha=1.0)
            
            axis[i][j].xaxis_date()
            axis[i][j].set_title(datadict[7][1][count])
            for k in axis[i, j].get_xticklabels():
                k.set_rotation(20)
            for k in axis[j, i].get_xticklabels():
                k.set_rotation(20)

            count += 1

    plt.plot()



plt.show()
