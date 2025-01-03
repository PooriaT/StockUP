import streamlit as st
from apis import stock_info, gemini_technical_analysis
from utils import session, invalid_data
from components import support_author


def general_ai_analysis_page():
    st.title("General AI Analysis of a Stock Symbol")
    symbol = session.set_session_state()
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()
    support_author.support_modal()
    if "longName" in stock_general_info:
        response_placeholder = st.empty()
        with st.spinner("Generating analysis..."):
            try:
                story = gemini_technical_analysis.get_gemini_response(
                    symbol,
                    stock_general_info,
                    stock.get_historical_data(period="1y", interval="5d"),
                    stock.get_news(),
                )
            except Exception as e:
                st.error(f"Error generating analysis: {e}", icon="🚨")

        response_placeholder.write(story)
    else:
        invalid_data.invalid_stock_symbol()


general_ai_analysis_page()
