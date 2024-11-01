import streamlit as st
from apis import stock_info
import plotly.graph_objects as go
import datetime


def home_page():
    st.title("Stock Dashboard")
    if "stock_symbol" not in st.session_state:
        st.session_state.stock_symbol = "AAPL"
    symbol = st.text_input("Enter stock symbol:", st.session_state.stock_symbol)
    st.session_state.stock_symbol = symbol
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()

    if "longName" in stock_general_info:
        st.header("General Information")

        st.write(f"**Company Name:** {stock_general_info['longName']}")
        st.write(f"**Country:** {stock_general_info['country']}")
        st.write(f"**City:** {stock_general_info['city']}")
        st.write(f"**Industry:** {stock_general_info['industry']}")
        st.write(f"**Sector:** {stock_general_info['sector']}")
        st.write(f"**Business Summary:** {stock_general_info['longBusinessSummary']}")
        finance_container = st.container()
        finance_container.subheader("**Finance Information:**")
        finance_container.write(
            f"**Current Price:** {stock_general_info['currentPrice']}"
        )
        fin_col01, fin_col02 = finance_container.columns(2)
        fin_col01.write(f"**Previous Close:** {stock_general_info['previousClose']}")
        fin_col01.write(f"**Open:** {stock_general_info['open']}")
        fin_col01.write(f"**Day Low:** {stock_general_info['dayLow']}")
        fin_col01.write(f"**Day High:** {stock_general_info['dayHigh']}")
        fin_col01.write(f"**Volume:** {stock_general_info['volume']}")
        fin_col01.write(f"**Average Volume:** {stock_general_info['averageVolume']}")
        fin_col01.write(
            f"**Average Volume (10 days):** {stock_general_info['averageVolume10days']}"
        )
        if "bid" in stock_general_info:
            fin_col01.write(
                f"**Bid:** {stock_general_info['bid']} * {stock_general_info['bidSize']}"
            )
        if "ask" in stock_general_info:
            fin_col01.write(
                f"**Ask:** {stock_general_info['ask']} * {stock_general_info['askSize']}"
            )
        fin_col02.write(f"**Market Cap:** {stock_general_info['marketCap']}")
        fin_col02.write(f"**52 Week Low:** {stock_general_info['fiftyTwoWeekLow']}")
        fin_col02.write(f"**52 Week High:** {stock_general_info['fiftyTwoWeekHigh']}")
        fin_col02.write(f"**50 Day Average:** {stock_general_info['fiftyDayAverage']}")
        fin_col02.write(
            f"**200 Day Average:** {stock_general_info['twoHundredDayAverage']}"
        )
        fin_col02.write(f"**Currency:** {stock_general_info['currency']}")
        fin_col02.write(f"**Exchange:** {stock_general_info['exchange']}")
        fin_col02.write(
            f"**Enterprise Value:** {stock_general_info['enterpriseValue']}"
        )
        finance_container.divider()
        fin_col11, fin_col12 = finance_container.columns(2)
        fin_col11.write(
            f"**Target High Price:** {stock_general_info['targetHighPrice']}"
        )
        fin_col11.write(f"**Target Low Price:** {stock_general_info['targetLowPrice']}")
        fin_col11.write(
            f"**Target Mean Price:** {stock_general_info['targetMeanPrice']}"
        )
        fin_col11.write(
            f"**Target Median Price:** {stock_general_info['targetMedianPrice']}"
        )
        fin_col12.write(
            f"**Recommendation Mean:** {stock_general_info['recommendationMean']}"
        )
        fin_col12.write(
            f"**Recommendation Key:** {stock_general_info['recommendationKey']}"
        )
        fin_col12.write(
            f"**Number of Analyst Opinions:** {stock_general_info['numberOfAnalystOpinions']}"
        )

        st.header("Historical Data")
        (
            hist_tab_1d,
            hist_tab_5d,
            hist_tab_1m,
            hist_tab_6m,
            hist_tab_1y,
            hist_tab_5y,
            hist_tab_all,
        ) = st.tabs(["1D", "5D", "1M", "6M", "1Y", "5Y", "All"])
        with hist_tab_1d:
            hist_1d = stock.get_historical_data(period="1d", interval="1m")
            fig = go.Figure(
                data=[
                    go.Candlestick(
                        x=hist_1d.index,
                        open=hist_1d["Open"],
                        high=hist_1d["High"],
                        low=hist_1d["Low"],
                        close=hist_1d["Close"],
                    )
                ]
            )
            st.plotly_chart(fig, use_container_width=True)
        with hist_tab_5d:
            hist_5d = stock.get_historical_data(period="5d", interval="30m")
            fig = go.Figure([go.Scatter(x=hist_5d.index, y=hist_5d["Close"])])
            st.plotly_chart(fig, use_container_width=True)
        with hist_tab_1m:
            hist_1m = stock.get_historical_data(period="1mo", interval="1d")
            fig = go.Figure([go.Scatter(x=hist_1m.index, y=hist_1m["Close"])])
            st.plotly_chart(fig, use_container_width=True)
        with hist_tab_6m:
            hist_6m = stock.get_historical_data(period="6mo", interval="5d")
            fig = go.Figure([go.Scatter(x=hist_6m.index, y=hist_6m["Close"])])
            st.plotly_chart(fig, use_container_width=True)
        with hist_tab_1y:
            hist_1y = stock.get_historical_data(period="1y", interval="1wk")
            fig = go.Figure([go.Scatter(x=hist_1y.index, y=hist_1y["Close"])])
            st.plotly_chart(fig, use_container_width=True)
        with hist_tab_5y:
            hist_5y = stock.get_historical_data(period="5y", interval="1mo")
            fig = go.Figure([go.Scatter(x=hist_5y.index, y=hist_5y["Close"])])
            st.plotly_chart(fig, use_container_width=True)
        with hist_tab_all:
            hist_all = stock.get_historical_data(period="max", interval="3mo")
            fig = go.Figure([go.Scatter(x=hist_all.index, y=hist_all["Close"])])
            st.plotly_chart(fig, use_container_width=True)

        news_container = st.header("News")
        news_container = st.container()
        for item in stock.get_news():
            news_container.subheader(item["title"])
            news_container.write(f"Publisher: {item['publisher']}")
            news_container.write(
                f"Published on: {datetime.datetime.fromtimestamp(item['providerPublishTime'])}"
            )
            news_container.write(f"[Read more]({item['link']})")
            news_container.write("_" * 50)

    else:
        st.write("Please enter a valid stock symbol to get the information.")


home_page()
