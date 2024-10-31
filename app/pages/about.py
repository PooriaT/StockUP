import streamlit as st


def about_page():
    st.title("About")

    st.write(
        """
        Welcome to StockUP, an AI-driven stock market analysis tool designed to provide 
        insightful information on stocks. This application is a prototype and serves as an 
        educational platform to demonstrate how AI can be leveraged in financial analysis.
        
        Features:
        - Easy-to-use interface for retrieving general stock information, historical data, 
          and news updates for any given stock symbol.
        - Utilizes the Gemini AI platform to generate detailed reports and trading 
          recommendations based on the latest available data.
        
        DISCLAIMER: Please note that this is a prototype and should not be used for actual investment 
        decisions. All information is provided for educational purposes only, and the use 
        of this application is at your own risk.
        """
    )

    st.write("Project Link: [GitHub Repository](https://github.com/PooriaT/StockUP)")
    st.write("Support the developer: [Buy me a Book](https://buymeacoffee.com/pooria7)")
    st.write("Follow the builder on X: [Pooria's X](https://x.com/PooriaTaghdiri)")


about_page()
