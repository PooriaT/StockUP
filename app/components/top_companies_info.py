from setup import environment
from apis import stock_info


def get_top_companies_news():
    stock_news = {}
    for symbol in environment.TOP_COMPANIES_LIST:
        stock = stock_info.StockInfo(symbol)
        stock_general_info = stock.get_general_info()

        if "longName" in stock_general_info:
            stock_news[symbol] = stock.get_news()
    return stock_news


def get_top_companies_historical_price(period="1y", interval="1d"):
    stock_historical_price = {}
    for symbol in environment.TOP_COMPANIES_LIST:
        stock = stock_info.StockInfo(symbol)
        stock_general_info = stock.get_general_info()

        if "longName" in stock_general_info:
            stock_historical_price[symbol] = stock.get_historical_data(
                period=period, interval=interval
            )
    return stock_historical_price
