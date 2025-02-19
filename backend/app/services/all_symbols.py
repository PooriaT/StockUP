import requests

URL = "https://api.twelvedata.com/stocks"


def get_all_symbols():
    stocks_data = requests.get(URL).json()
    list_of_stocks = []

    number_of_stocks = stocks_data["count"]
    stocks = stocks_data["data"]

    for i in range(number_of_stocks):
        if stocks[i]["country"] == "United States" and stocks[i]["exchange"] in [
            "NASDAQ",
            "NYSE",
        ]:
            list_of_stocks.append(stocks[i]["symbol"])

    return list_of_stocks


if __name__ == "__main__":
    print(get_all_symbols())
