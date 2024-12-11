import streamlit as st
from components import top_companies_info
from setup import environment
import datetime
import plotly.graph_objects as go


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

    companies_news = top_companies_info.get_top_companies_news()
    companies_historical_price = top_companies_info.get_top_companies_historical_price(
        period="1y", interval="1d"
    )
    companies_list = environment.TOP_COMPANIES_LIST
    number_of_companies = len(companies_list)
    st.write(
        """
        PRICE CHART OF TOP COMPANIES
        """
    )

    charts_container = st.container()
    charts_columns = charts_container.columns(2)
    for i in range(0, number_of_companies, 2):
        with charts_columns[0]:
            fig = go.Figure(
                data=[
                    go.Candlestick(
                        x=companies_historical_price[companies_list[i]].index,
                        open=companies_historical_price[companies_list[i]]["Open"],
                        high=companies_historical_price[companies_list[i]]["High"],
                        low=companies_historical_price[companies_list[i]]["Low"],
                        close=companies_historical_price[companies_list[i]]["Close"],
                    )
                ]
            )
            fig.update_layout(
                title=companies_list[i],
                yaxis_title="Price (USD)",
                xaxis_title="Date",
            )

            st.plotly_chart(fig, use_container_width=True)
        if i + 1 < number_of_companies:
            with charts_columns[1]:
                fig = go.Figure(
                    data=[
                        go.Candlestick(
                            x=companies_historical_price[companies_list[i + 1]].index,
                            open=companies_historical_price[companies_list[i + 1]][
                                "Open"
                            ],
                            high=companies_historical_price[companies_list[i + 1]][
                                "High"
                            ],
                            low=companies_historical_price[companies_list[i + 1]][
                                "Low"
                            ],
                            close=companies_historical_price[companies_list[i + 1]][
                                "Close"
                            ],
                        )
                    ]
                )
                fig.update_layout(
                    title=companies_list[i + 1],
                    yaxis_title="Price (USD)",
                    xaxis_title="Date",
                )
                st.plotly_chart(fig, use_container_width=True)

    st.write(
        """
        LATEST NEWS OF TOP COMPANIES
        """
    )

    tabs = st.tabs(companies_list)

    for i in range(number_of_companies):
        with tabs[i]:
            # st.write(companies_news[companies_list[i]])
            news_container = st.container()
            for item in companies_news[companies_list[i]]:
                news_container.subheader(item["title"])
                if "thumbnail" in item and len(item["thumbnail"]["resolutions"]) > 1:
                    news_container.image(item["thumbnail"]["resolutions"][1]["url"])
                news_container.write(f"Publisher: {item['publisher']}")
                news_container.write(
                    f"Published on: {datetime.datetime.fromtimestamp(item['providerPublishTime'])}"
                )
                news_container.write(f"[Read more]({item['link']})")
                news_container.write("_" * 50)


home_page()
