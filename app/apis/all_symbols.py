import json
import os
import yfinance as yf

FILE_DIR = os.path.join(
    os.path.dirname(__file__), "../../static/json/company_tickers.json"
)


def get_all_symbols():
    symbols = []
    try:
        with open(FILE_DIR) as f:
            data = json.load(f)
            n = len(data)
            for i in range(n):
                symbols.append(data[str(i)]["ticker"])
    except FileNotFoundError:
        print(f"File not found: {FILE_DIR}")

    return symbols
