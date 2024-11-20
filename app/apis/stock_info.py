import yfinance as yf
import json


class StockInfo:
    def __init__(self, symbol):
        self.symbol = symbol
        self.stock = yf.Ticker(symbol)

    def get_general_info(self):
        try:
            return self.stock.info
        except json.JSONDecodeError:
            return {}

    def get_historical_data(self, period, interval):
        return self.stock.history(period=period, interval=interval)

    def get_news(self):
        return self.stock.news

    @staticmethod
    def get_batch_download(stocks, period, interval):
        return yf.download(stocks, period=period, interval=interval)
