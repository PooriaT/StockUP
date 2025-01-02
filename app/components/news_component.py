import datetime
import streamlit as st


def get_news_per_stock(news_container, item):
    content = item["content"]
    news_container.subheader(content["title"])
    if (
        "thumbnail" in content
        and content["thumbnail"] is not None
        and len(content["thumbnail"]["resolutions"]) > 1
    ):
        news_container.image(content["thumbnail"]["resolutions"][1]["url"])
    news_container.write(f"Publisher: {content['provider']['displayName']}")
    if "summary" in content and content["summary"] is not None:
        news_container.write(f"Summary: {content['summary']}")
    news_container.write(
        f"Published on: {datetime.datetime.strptime(content['pubDate'], '%Y-%m-%dT%H:%M:%SZ')}"
    )
    if content["clickThroughUrl"] is not None:
        news_container.write(f"[Read more]({content['clickThroughUrl']['url']})")
    news_container.write("_" * 50)
