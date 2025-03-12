import google.generativeai as genai
import dotenv
import os
from setup import environment

dotenv.load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name=environment.GEMINI_MODEL_NAME)


def get_gemini_response(SYMBOL, stock_general_info, stock_history, stock_news):
    prompt = f"""
    You are an expert financial analyst and stock trader with deep knowledge of technical analysis, 
    fundamental analysis, and market trends. Analyze the following stock data for {SYMBOL} and 
    provide a comprehensive report and trading recommendation.
    Stock Information:
    {stock_general_info}
    Historical Data:
    {stock_history}
    Recent News:
    {stock_news}
    Based on the provided information, perform the following analysis:

    Technical Analysis:

    Identify key support and resistance levels
    Calculate and interpret moving averages (50-day and 200-day)
    Analyze volume trends
    Identify any significant chart patterns or candlestick formations
    Calculate and interpret technical indicators (e.g., RSI, MACD, Bollinger Bands)


    Fundamental Analysis:

    Evaluate key financial ratios (P/E, P/B, Debt/Equity, etc.)
    Assess the company's revenue and earnings growth
    Compare the stock's valuation to industry peers


    News and Sentiment Analysis:

    Summarize the key points from recent news
    Assess the overall sentiment (positive, neutral, or negative)
    Identify any potential catalysts or risks mentioned in the news


    Market Trend Analysis:

    Determine the overall market trend (bullish, bearish, or neutral)
    Compare the stock's performance to relevant market indices


    Trading Recommendation:

    Provide a clear recommendation: Strong Buy, Buy, Hold, Sell, or Strong Sell
    Explain the rationale behind your recommendation
    Suggest entry and exit points, including stop-loss and take-profit levels
    Estimate the potential upside and downside risks


    Risk Assessment:

    Identify key risks factors for this stock
    Provide a risk rating (Low, Medium, or High) and explain your reasoning


    Short-term and Long-term Outlook:

    Provide separate outlooks for short-term (1-3 months) and long-term (6-12 months) horizons
    Explain any differences between these outlooks


    Alternative Scenarios:

    Briefly describe potential bullish and bearish scenarios that could impact your analysis



    Conclude your analysis with a summary of the most important points and any final thoughts or 
    considerations for potential investors.
    Remember to use clear, concise language and provide specific data points to support your analysis 
    and recommendations. Your goal is to give a comprehensive yet actionable insight into the stock's potential 
    performance. 
    At the end of the response, provide a declaimer that the analysis is for informational purposes only and 
    should not be considered as financial advice. This last sentence should be written all letters in UPPERCASE.
    """

    response = model.generate_content(prompt)
    return response.text
