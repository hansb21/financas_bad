
from functions import *

valores = []
for i in ['ETH','XMR', 'AID', 'ZRX']:
    Read(i, "USD")

plot(datadict)
plt.show()
