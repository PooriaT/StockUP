import pytest
from unittest.mock import patch
from app.apis.stock_info import StockInfo


@pytest.fixture
def mock_ticker():
    with patch("app.apis.stock_info.yf.Ticker") as mock_ticker:
        yield mock_ticker


def test_get_general_info(mock_ticker):
    mock_ticker.return_value.info = {"symbol": "AAPL", "marketCap": 2500000000000}

    stock_info = StockInfo("AAPL")
    general_info = stock_info.get_general_info()

    assert general_info["symbol"] == "AAPL"
    assert general_info["marketCap"] == 2500000000000


def test_get_historical_data(mock_ticker):
    mock_ticker.return_value.history.return_value = {
        "Date": ["2023-09-20"],
        "Close": [150.0],
    }

    stock_info = StockInfo("AAPL")
    historical_data = stock_info.get_historical_data("1d", "1m")

    assert historical_data["Date"] == ["2023-09-20"]
    assert historical_data["Close"] == [150.0]


def test_get_news(mock_ticker):
    mock_ticker.return_value.news = [
        {"title": "Apple releases new product", "link": "example.com"}
    ]

    stock_info = StockInfo("AAPL")
    news = stock_info.get_news()

    assert len(news) == 1
    assert news[0]["title"] == "Apple releases new product"
    assert news[0]["link"] == "example.com"
