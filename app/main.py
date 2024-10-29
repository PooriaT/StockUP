import streamlit as st

if __name__ == "__main__":
    home_page = st.Page("pages/home.py", title="HOME", icon=":material/home:")
    ai_analysis_page = st.Page(
        "pages/ai_analysis.py", title="AI ANALYSIS", icon=":material/science:"
    )
    about_page = st.Page(
        "pages/about.py", title="ABOUT", icon=":material/format_quote:"
    )
    pg = st.navigation([home_page, ai_analysis_page, about_page])
    pg.run()
