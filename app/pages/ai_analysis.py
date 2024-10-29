import streamlit as st
from apis import stock_info, gemini


def ai_analysis_page():
    st.title("AI Analysis")
    symbol = st.text_input("Enter stock symbol:", "AAPL")
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()
    if "longName" in stock_general_info:
        response_placeholder = st.empty()
        with st.spinner("Generating analysis..."):
            story = gemini.get_gemini_response(
                symbol,
                stock_general_info,
                stock.get_historical_data(period="1y", interval="5d"),
                stock.get_news(),
            )

        response_placeholder.write(story)
    else:
        st.write("Please enter a valid stock symbol to get the information.")


ai_analysis_page()
