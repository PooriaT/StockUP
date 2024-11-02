import streamlit as st
from apis import stock_info, gemini
from utils import session, invalid_data


def ai_analysis_page():
    st.title("AI Analysis")
    symbol = session.set_session_state()
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()
    if "longName" in stock_general_info:
        response_placeholder = st.empty()
        # with st.spinner("Generating analysis..."):
        #     story = gemini.get_gemini_response(
        #         symbol,
        #         stock_general_info,
        #         stock.get_historical_data(period="1y", interval="5d"),
        #         stock.get_news(),
        #     )

        # response_placeholder.write(story)
        with st.spinner("Generating analysis..."):
            response_placeholder.write_stream(
                gemini.get_gemini_response(
                    symbol,
                    stock_general_info,
                    stock.get_historical_data(period="1y", interval="5d"),
                    stock.get_news(),
                )
            )
    else:
        invalid_data.invalid_stock_symbol()


ai_analysis_page()
