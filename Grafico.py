import matplotlib.pyplot as plt
import mpl_finance
import numpy as np

class Grafico:

    def __init__(self, candlestick_Info, average_Info):
        self.candlestick_Info = candlestick_Info
        self.average_Info = average_Info

    def Candlestick(self):
        figura, axis = plt.subplot(figsize=(10, 5))
        quotes = [tuple([
                    self.candlestick_Info["time"][index],
                    self.candlestick_Info["open"][index],
                    self.candlestick_Info["high"][index],
                    self.candlestick_Info["low"][index],
                    self.candlestick_Info["close"][index]
                
                ])for index in range(len(self.candlestick_Info["time"]))]

        mpl_finance.candlestick_ohlc(axis, quotes, colordown='r', colorup='g')
        axis.xaxis_date()
        plt.xticks(rotation=20)
        plt.title("Plot")
        plt.title("Data")
        plt.title("Valor")
        plt.plot()
    def graph_all(self):
        figure, axis1 = plt.subplots(figsize = (10,5))
        quotes = []
        for index in range(len(self.candlestick_Info["time"])):
            quotes.append(tuple ([self.candlestick_Info["time"][index], self.candlestick_Info["open"][index], self.candlestick_Info["high"][index], self.candlestick_Info["low"][index], self.candlestick_Info["close"][index],]))
        mpl_finance.candlestick_ohlc(axis1, quotes, colordown='r', colorup='g')
        axis1.plot(self.average_Info["datas"], self.average_Info["media"], 'r--', alpha=0.75, label = "Média Móvel")
        axis1.plot(self.candlestick_Info["time"], self.candlestick_Info["volume"], 'b', alpha=0.5, label = "Volume")
        axis1.margins(x=0, y=-0.25) #Zoom
        axis1.xaxis_date()
        plt.xticks(rotation=20)
        plt.title("Simple Plot")
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.show()