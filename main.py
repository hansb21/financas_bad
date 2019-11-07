from Coin import Coins
from Grafico import Grafico

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

Coin = Coins("BTC", "CNY", 100)
movingAvegare = Coin.send_SMA()
candleStick = Coin.send_Crypto()
graph = Grafico(candleStick, movingAvegare)
graph.graph_all()
