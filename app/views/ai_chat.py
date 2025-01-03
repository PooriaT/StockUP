import streamlit as st
from apis import stock_info, gemini_with_history
from utils import session, invalid_data
from components import support_author


def ai_chat():
    st.title("Interactive AI Chat")
    symbol = session.set_session_state()
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()
    support_author.support_modal()

    user_prompt = st.text_area(
        """Ask your questions from AI based on the chosen stock symbol 
        (e.g., What is the best strategy for investing X dollars in this stock?)""",
        "",
    )
    if user_prompt:
        if "longName" in stock_general_info:
            response_placeholder = st.empty()
            with st.spinner("Generating analysis..."):
                try:
                    story = gemini_with_history.get_gemini_response(
                        symbol,
                        stock_general_info,
                        stock.get_historical_data(period="1y", interval="5d"),
                        stock.get_news(),
                        user_prompt,
                    )
                except Exception as e:
                    st.error(f"Error generating analysis: {e}", icon="🚨")

            response_placeholder.write(story)
        else:
            invalid_data.invalid_stock_symbol()


ai_chat()
