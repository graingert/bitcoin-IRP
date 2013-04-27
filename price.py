from __future__ import print_function
import sys
import requests

from math import log10, floor

for market in requests.get("http://api.bitcoincharts.com/v1/markets.json").json():
    if market["symbol"] == "mtgoxUSD":
        price = int(round(market["close"], -int(floor(log10(market["close"])))))

with open(sys.argv[1], 'w') as f:
    print("over \\${price}".format(price=price), end="", file=f)
    print(r"\footnote{\url{http://bitcoincharts.com/markets/mtgoxUSD.html}}", end="", file=f)
