import streamlit as st

if __name__ == "__main__":
    st.set_page_config(
        page_title="StockUP",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    home_page = st.Page("pages/home.py", title="Home", icon=":material/home:")
    stock_info_page = st.Page(
        "pages/stock_info.py", title="Stock Information", icon=":material/query_stats:"
    )
    ai_analysis_page = st.Page(
        "pages/ai_analysis.py", title="AI ANALYSIS", icon=":material/science:"
    )
    about_page = st.Page(
        "pages/about.py", title="ABOUT", icon=":material/format_quote:"
    )
    pg = st.navigation([home_page, stock_info_page, ai_analysis_page, about_page])
    pg.run()
