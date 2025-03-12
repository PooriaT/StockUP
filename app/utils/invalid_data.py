import streamlit as st


def invalid_stock_symbol():
    st.warning("Please enter a valid stock symbol to get the information.", icon="⚠️")
