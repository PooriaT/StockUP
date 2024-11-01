from math import e
import streamlit as st
from apis import stock_info
from utils import session, invalid_data


def home_page():
    st.title("Welcome to StockUP")
    st.image("./static/img/home_page_img_1.webp", width=400)
    st.write(
        """
        StockUP is an AI-driven stock market analysis tool designed to provide 
        insightful information on stocks. This application is a prototype and serves 
        as an educational platform to demonstrate how AI can be leveraged in financial 
        analysis.
        """
    )
    st.write(
        """
        Features:
        - Easy-to-use interface for retrieving general stock information, historical data, 
          and news updates for any given stock symbol.
        - Utilizes the Gemini AI platform to generate detailed reports and trading 
          recommendations based on the latest available data.
        """
    )
    st.write(
        """
        First insert a stock symbol and get started.
        """
    )

    symbol = session.set_session_state()
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()

    if "longName" in stock_general_info:
        st.write(
            """
            Now you can navigate to StocK Information page to get the stock information. \n
            [STOCK INFO](./stock_info) \n
            or jump into AI Analysis page.\n
            [AI ANALYSIS](./ai_analysis)
            """
        )
    else:
        invalid_data.invalid_stock_symbol()

    st.write(
        """
        Refer to the [About page](./about) for more information.
        """
    )


home_page()
