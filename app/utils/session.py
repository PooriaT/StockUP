import streamlit as st
from apis.all_symbols import get_all_symbols


def set_session_state():
    """Get the stock symbol from the user or session state"""
    if "stock_symbol" not in st.session_state:
        st.session_state.stock_symbol = "AAPL"
    user_input = st.text_input("Enter stock symbol:", st.session_state.stock_symbol)

    user_input = user_input.upper()
    symbols = [symbol for symbol in get_all_symbols() if user_input in symbol]

    if len(symbols) > 0:
        user_input = symbols[0]

    st.session_state.stock_symbol = user_input
    return user_input
