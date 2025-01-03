import streamlit as st
from apis import stock_info
from utils import session, invalid_data
import plotly.graph_objects as go
from components import news_component


def stock_info_page():
    """
    Displays a stock dashboard with general information and financial data.

    This function uses Streamlit to create a user interface that allows users
    to enter a stock symbol and view the corresponding data.
    """
    st.title("Stock Dashboard")
    symbol = session.set_session_state()
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()

    if "longName" in stock_general_info:
        st.header("General Information")

        if (
            "website" in stock_general_info
            and stock_general_info["website"] is not None
        ):
            st.write(
                f"**Company Name:** [{stock_general_info['longName']}]({stock_general_info['website']})"
            )
        else:
            st.write(f"**Company Name:** {stock_general_info['longName']}")
        if "country" in stock_general_info and "city" in stock_general_info:
            st.write(f"**Country:** {stock_general_info['country']}")
            st.write(f"**City:** {stock_general_info['city']}")
        if "industry" in stock_general_info and "sector" in stock_general_info:
            st.write(f"**Industry:** {stock_general_info['industry']}")
            st.write(f"**Sector:** {stock_general_info['sector']}")
        if "longBusinessSummary" in stock_general_info:
            st.write(
                f"**Business Summary:** \n\n{stock_general_info['longBusinessSummary']}"
            )
        finance_container = st.container()
        if "currentPrice" in stock_general_info:
            finance_container.subheader("**Finance Information:**")
            finance_container.write(
                f"**Current Price:** {stock_general_info['currentPrice']}"
            )
            fin_col01, fin_col02 = finance_container.columns(2)
            fin_col01.write(
                f"**Previous Close:** {stock_general_info['previousClose']}"
            )
            fin_col01.write(f"**Open:** {stock_general_info['open']}")
            fin_col01.write(f"**Day Low:** {stock_general_info['dayLow']}")
            fin_col01.write(f"**Day High:** {stock_general_info['dayHigh']}")
            fin_col01.write(
                f"**Volume:** {format(int(stock_general_info['volume']), ',d')}"
            )
            fin_col01.write(
                f"**Average Volume:** {format(int(stock_general_info['averageVolume']), ',d')}"
            )
            fin_col01.write(
                f"**Average Volume (10 days):** {format(int(stock_general_info['averageVolume10days']), ',d')}"
            )
            if "bid" in stock_general_info:
                fin_col01.write(
                    f"**Bid:** {stock_general_info['bid']} * {stock_general_info['bidSize']}"
                )
            if "ask" in stock_general_info:
                fin_col01.write(
                    f"**Ask:** {stock_general_info['ask']} * {stock_general_info['askSize']}"
                )
            fin_col02.write(
                f"**Market Cap:** {format(int(stock_general_info['marketCap']), ',d')}"
            )
            fin_col02.write(f"**52 Week Low:** {stock_general_info['fiftyTwoWeekLow']}")
            fin_col02.write(
                f"**52 Week High:** {stock_general_info['fiftyTwoWeekHigh']}"
            )
            if (
                "trailingPE" in stock_general_info
                and stock_general_info["trailingPE"] is not None
            ):
                fin_col02.write(f"**Trailing PE:** {stock_general_info['trailingPE']}")
            if (
                "forwardPE" in stock_general_info
                and stock_general_info["forwardPE"] is not None
            ):
                fin_col02.write(f"**Forward PE:** {stock_general_info['forwardPE']}")
            fin_col02.write(
                f"**50 Day Average:** {stock_general_info['fiftyDayAverage']}"
            )
            fin_col02.write(
                f"**200 Day Average:** {stock_general_info['twoHundredDayAverage']}"
            )
            fin_col02.write(f"**Currency:** {stock_general_info['currency']}")
            fin_col02.write(f"**Exchange:** {stock_general_info['exchange']}")
            fin_col02.write(
                f"**Enterprise Value:** {format(int(stock_general_info['enterpriseValue']), ',d')}"
            )
            finance_container.divider()
            fin_col11, fin_col12 = finance_container.columns(2)
            if "targetHighPrice" in stock_general_info:
                fin_col11.write(
                    f"**Target High Price:** {stock_general_info['targetHighPrice']}"
                )
            if "targetLowPrice" in stock_general_info:
                fin_col11.write(
                    f"**Target Low Price:** {stock_general_info['targetLowPrice']}"
                )
            if "targetMeanPrice" in stock_general_info:
                fin_col11.write(
                    f"**Target Mean Price:** {stock_general_info['targetMeanPrice']}"
                )
            if "targetMedianPrice" in stock_general_info:
                fin_col11.write(
                    f"**Target Median Price:** {stock_general_info['targetMedianPrice']}"
                )
            if "recommendationMean" in stock_general_info:
                fin_col12.write(
                    f"**Recommendation Mean:** {stock_general_info['recommendationMean']}"
                )
            if "recommendationKey" in stock_general_info:
                fin_col12.write(
                    f"**Recommendation Key:** {stock_general_info['recommendationKey']}"
                )
            if "numberOfAnalystOpinions" in stock_general_info:
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
                hist_5d = stock.get_historical_data(period="5d", interval="15m")
                fig = go.Figure([go.Scatter(x=hist_5d.index, y=hist_5d["Close"])])
                st.plotly_chart(fig, use_container_width=True)
            with hist_tab_1m:
                hist_1m = stock.get_historical_data(period="1mo", interval="1h")
                fig = go.Figure([go.Scatter(x=hist_1m.index, y=hist_1m["Close"])])
                st.plotly_chart(fig, use_container_width=True)
            with hist_tab_6m:
                hist_6m = stock.get_historical_data(period="6mo", interval="1d")
                fig = go.Figure([go.Scatter(x=hist_6m.index, y=hist_6m["Close"])])
                if hist_6m.empty:
                    st.error("No data available for this period")
                else:
                    st.plotly_chart(fig, use_container_width=True)
            with hist_tab_1y:
                hist_1y = stock.get_historical_data(period="1y", interval="1d")
                fig = go.Figure([go.Scatter(x=hist_1y.index, y=hist_1y["Close"])])
                if hist_1y.empty:
                    st.error("No data available for this period")
                else:
                    st.plotly_chart(fig, use_container_width=True)
            with hist_tab_5y:
                hist_5y = stock.get_historical_data(period="5y", interval="1d")
                fig = go.Figure([go.Scatter(x=hist_5y.index, y=hist_5y["Close"])])
                if hist_5y.empty:
                    st.error("No data available for this period")
                else:
                    st.plotly_chart(fig, use_container_width=True)
            with hist_tab_all:
                hist_all = stock.get_historical_data(period="max", interval="1d")
                fig = go.Figure([go.Scatter(x=hist_all.index, y=hist_all["Close"])])
                st.plotly_chart(
                    fig, use_container_width=True, key="unique_key_hist_all"
                )

            news_container = st.header("News")
            news_container = st.container()
            for item in stock.get_news():
                news_component.get_news_per_stock(news_container, item)

        else:
            invalid_data.invalid_stock_symbol()


stock_info_page()
