import yfinance as yf


class StockInfo:
    def __init__(self, symbol):
        self.symbol = symbol
        self.stock = yf.Ticker(symbol)

    def get_general_info(self):
        return self.stock.info

    def get_historical_data(self, period, interval):
        return self.stock.history(period=period, interval=interval)

    def get_news(self):
        return self.stock.news
