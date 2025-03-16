from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from app.services import stock_info, gemini_technical_analysis, gemini_with_history
from app.setup import environment

app = FastAPI()

# CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://stockupforall.onrender.com, http://localhost:5173"
    ],  # Adjust this for deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/big_seven")
def read_root():
    companies_list = environment.TOP_COMPANIES_LIST
    number_of_companies = len(companies_list)
    big_seven_info = {}
    for company in companies_list:
        stock = stock_info.StockInfo(company)
        stock_history = stock.get_historical_data(period="1y", interval="1d")
        stock_history = stock_history.replace(
            [float("inf"), float("-inf")], None
        ).dropna()
        stock_news = stock.get_news()
        big_seven_info[company] = {
            "stock_history": stock_history.to_dict(),
            "stock_news": [dict(news) for news in stock_news],
        }
    return {
        "number_of_companies": number_of_companies,
        "big_seven_info": big_seven_info,
    }


@app.get("/stock/{symbol}")
def get_stock_info(symbol: str):
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()
    stock_history_1d = (
        stock.get_historical_data(period="1d", interval="1m")
        .replace([float("inf"), float("-inf")], None)
        .dropna()
    )
    stock_history_5d = (
        stock.get_historical_data(period="5d", interval="15m")
        .replace([float("inf"), float("-inf")], None)
        .dropna()
    )
    stock_history_1mo = (
        stock.get_historical_data(period="1mo", interval="1h")
        .replace([float("inf"), float("-inf")], None)
        .dropna()
    )
    stock_history_6mo = (
        stock.get_historical_data(period="6mo", interval="1d")
        .replace([float("inf"), float("-inf")], None)
        .dropna()
    )
    stock_history_1y = (
        stock.get_historical_data(period="1y", interval="1d")
        .replace([float("inf"), float("-inf")], None)
        .dropna()
    )
    stock_history_5y = (
        stock.get_historical_data(period="5y", interval="1d")
        .replace([float("inf"), float("-inf")], None)
        .dropna()
    )
    stock_history_all = (
        stock.get_historical_data(period="1y", interval="1d")
        .replace([float("inf"), float("-inf")], None)
        .dropna()
    )
    stock_news = stock.get_news()
    return {
        "stock_general_info": dict(stock_general_info),
        "stock_history_1d": stock_history_1d.to_dict(),
        "stock_history_5d": stock_history_5d.to_dict(),
        "stock_history_1mo": stock_history_1mo.to_dict(),
        "stock_history_6mo": stock_history_6mo.to_dict(),
        "stock_history_1y": stock_history_1y.to_dict(),
        "stock_history_5y": stock_history_5y.to_dict(),
        "stock_history_all": stock_history_all.to_dict(),
        "stock_news": [dict(news) for news in stock_news],
    }


@app.get("/ai_analysis/{symbol}")
def get_ai_analysis(symbol: str):
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()
    stock_history = (
        stock.get_historical_data(period="1y", interval="5d")
        .replace([float("inf"), float("-inf")], None)
        .dropna()
    )
    stock_news = stock.get_news()
    response = gemini_with_history.get_gemini_response(
        symbol,
        stock_general_info,
        stock_history.to_dict(),
        [dict(news) for news in stock_news],
    )
    return {"response": response}


@app.post("/ai_chatbot/{symbol}")
def get_ai_chatbot(symbol: str, user_prompt: str = Body(...)):
    stock = stock_info.StockInfo(symbol)
    stock_general_info = stock.get_general_info()
    stock_history = (
        stock.get_historical_data(period="1y", interval="5d")
        .replace([float("inf"), float("-inf")], None)
        .dropna()
    )
    stock_news = stock.get_news()
    response = gemini_with_history.get_gemini_response(
        symbol,
        stock_general_info,
        stock_history.to_dict(),
        [dict(news) for news in stock_news],
        user_prompt,
    )
    return {"response": response}
