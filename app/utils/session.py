import streamlit as st


def set_session_state():
    """Get the stock symbol from the user or session state"""
    if "stock_symbol" not in st.session_state:
        st.session_state.stock_symbol = "AAPL"
    symbol = st.text_input("Enter stock symbol:", st.session_state.stock_symbol)
    st.session_state.stock_symbol = symbol
    return symbol
