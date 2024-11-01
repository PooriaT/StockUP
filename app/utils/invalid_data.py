import streamlit as st


def invalid_stock_symbol():
    st.markdown(
        """
        <p style="color:red;background-color:yellow">
        Please enter a valid stock symbol to get the information.
        </p>
        """,
        unsafe_allow_html=True,
    )
