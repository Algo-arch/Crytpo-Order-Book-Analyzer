# Order Book Analyzer 

# Instead of looking at candles, it analyzes the actual market making liquidity. 
# The binance order books shows : Bids(buyers) and Asks(sellers)

# From this we calculates things like:
# Order book Imbalance

# Important metric ----> Imbalance = (Bid Volumne - Ask Volumne) / (Bid Volumne + Ask Volumne)

# If Imbalance > 0 ----> buyers are stronger
# If Imbalance < 0 ----> sellers are stronger

# If Imbalance near 0 ----> balanced
# Market Makers watch this constantly. 

# What our tool will do:
# 1) Connect to Binance API
# 2) Fetch Order Book Depth
# 3) Calculate :
# Bid liquidity
# Ask liquidity
# Order Book Imbalance

# Print real time signal. 

import requests
import pandas as pd
import time 


SYMBOL = "BTCUSDT"
LIMIT = "50"

BASE_URL = "https://api.binance.com/api/v3/depth"

def get_order_book():
    parameters = {"symbol":SYMBOL, "limit":LIMIT}

    response = requests.get(BASE_URL, params = parameters)
    data = response.json()

    bids = pd.DataFrame(data["bids"], columns = ["price","quantity"])
    asks = pd.DataFrame(data["asks"], columns = ["price", "quantity"])

    bids["quantity"] = bids["quantity"].astype(float)
    asks["quantity"] = asks["quantity"].astype(float)

    return bids, asks

def calculate_imbalance(bids, asks):
    bid_volumne = bids["quantity"].sum()
    ask_volumne = asks["quantity"].sum()

    imbalance = (bid_volumne - ask_volumne) / (bid_volumne + ask_volumne)

    return bid_volumne, ask_volumne, imbalance

def monitor_order_book():

    while True:

        bids, asks = get_order_book()

        bid_volume, ask_volume, imbalance = calculate_imbalance(bids, asks)

        print("---------------------------")
        print(f"Symbol:{SYMBOL}")
        print(f"bid liquidity:{bid_volume:.2f}")
        print(f"ask liquidity:{ask_volume:.2f}")
        print(f"Order book Imbalance:{imbalance:.4f}")

        if imbalance > 0.1:
            print("Market pressure : Buy side")
        elif imbalance < - 0.1:
            print("Market pressure : Sell side")
        else:
            print("Market pressure balanced")

        time.sleep(1)

if __name__ == "__main__":
    print("starting order book analyzer")

    monitor_order_book()
