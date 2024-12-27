import streamlit as st
from apis import stock_info, gemini_technical_analysis
from utils import session, invalid_data


def general_ai_analysis_page():
    st.title("General AI Analysis of a Stock Symbol")
    symbol = session.set_session_state()
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()
    support_modal()
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


@st.dialog("Support Us")
def support_modal():
    st.write(
        """
        <div style="display: flex; align-items: center;">
            <span style="margin-right: 1rem;">❤️</span>
            <span>
                Support the developer: <a href="https://buymeacoffee.com/pooria7" target="_blank">Buy me a Book</a>
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        """
        <div style="display: flex; align-items: center;">
            <span style="margin-right: 1rem;">❤️</span>
            <span>
                Follow the builder on X: <a href="https://x.com/PooriaTaghdiri" target="_blank">Pooria's X</a>
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


general_ai_analysis_page()
