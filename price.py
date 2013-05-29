from __future__ import print_function
import sys
import requests
import six

from math import log10, floor

def call_or_get(prop):
    if six.callable(prop):
        return prop()
    else:
        return prop

def one_sig_fig(price):
    sig = int(round(price, -int(floor(log10(price)))))
    return (sig, "over" if price-sig > 0 else "just under")

if __name__ == "__main__":
    for market in call_or_get(requests.get("http://api.bitcoincharts.com/v1/markets.json").json):
        if market["symbol"] == "mtgoxUSD":
            price, direction = one_sig_fig(market["close"])

    with open(sys.argv[1], 'w') as f:
        print("{direction} \\${price}".format(
            price=price,
            direction=direction
        ), end="", file=f)
        print(r"\footnote{\url{http://bitcoincharts.com/markets/mtgoxUSD.html}}%", file=f)
