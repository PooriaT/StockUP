import streamlit as st
from components import top_companies_news
from setup import environment
import datetime


def home_page():
    st.title("Welcome to StockUP")
    st.image("./static/img/home_page_img_1.webp", width=400)
    st.write(
        """
        StockUP is an AI-driven stock market analysis tool designed to provide 
        insightful information on stocks. This application is a prototype and serves 
        as an educational platform to demonstrate how AI can be leveraged in financial 
        analysis.
        """
    )
    st.write(
        """
        Features:
        - Easy-to-use interface for retrieving general stock information, historical data, 
          and news updates for any given stock symbol.
        - Utilizes the Gemini AI platform to generate detailed reports and trading 
          recommendations based on the latest available data.
        """
    )
    st.write(
        """
        LATEST NEWS OF TOP COMPANIES
        """
    )

    companies_news = top_companies_news.get_top_companies_news()
    companies_list = environment.TOP_COMPANIES_LIST
    number_of_companies = len(companies_list)

    tabs = st.tabs(companies_list)

    for i in range(number_of_companies):
        with tabs[i]:
            # st.write(companies_news[companies_list[i]])
            news_container = st.container()
            for item in companies_news[companies_list[i]]:
                news_container.subheader(item["title"])
                if "thumbnail" in item:
                    news_container.image(item["thumbnail"]["resolutions"][1]["url"])
                news_container.write(f"Publisher: {item['publisher']}")
                news_container.write(
                    f"Published on: {datetime.datetime.fromtimestamp(item['providerPublishTime'])}"
                )
                news_container.write(f"[Read more]({item['link']})")
                news_container.write("_" * 50)


home_page()
