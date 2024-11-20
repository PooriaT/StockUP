from Projects.StockUP.app.apis import ai_technical_analysis
import streamlit as st
from apis import stock_info
from utils import session, invalid_data


def ai_analysis_page():
    st.title("AI Analysis")
    symbol = session.set_session_state()
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()
    if "longName" in stock_general_info:
        response_placeholder = st.empty()
        with st.spinner("Generating analysis..."):
            try:
                story = ai_technical_analysis.get_ai_technical_analysis(
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


ai_analysis_page()
