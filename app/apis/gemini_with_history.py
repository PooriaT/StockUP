import google.generativeai as genai
import dotenv
import os

dotenv.load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")


def get_gemini_response(
    SYMBOL, stock_general_info, stock_history, stock_news, user_prompt=""
):
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
    Also, the user provided some more information about the stock. Here is the user prompt:
    {user_prompt}
    The user might provide some information about their trading strategy, their risk tolerance, or their investment goals, or
    their budgets and etc.
    First action is to check the user prompt. If it is unrelated to the stock marker, then return some response like this:
    "The user prompt is not relevant to the stock market. Please provide a valid prompt."
    Otherwise, continue with the analysis.
    Based on the provided information, provide some technical analysis, fundamental analysis,
    news and sentiment analysis, market trend analysis, and trading recommendation.
    for example suggest entry and exit points, including stop-loss and take-profit levels.
    The response should be in a well-structured and easy to understand format, and the analysis should be based on the latest available data.
    At the end of the response, provide a declaimer that the analysis is for informational purposes only and 
    should not be considered as financial advice. This last sentence should be written all letters in UPPERCASE.
    """

    response = model.generate_content(prompt)
    return response.text
