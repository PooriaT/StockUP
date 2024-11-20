import google.generativeai as genai
import stock_info
import all_symbols
import dotenv
import os
import time

dotenv.load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")


def find_penny_stocks():
    penny_stocks = {}

    stocks = all_symbols.get_all_symbols()
    stocks_with_info = stock_info.StockInfo.get_batch_download(
        stocks, period="1d", interval="1d"
    )

    for col in stocks_with_info.columns:
        if col[0] == "Close":
            symbol = col[1]
            close = stocks_with_info[col].iloc[-1]
            if close < 1:
                penny_stocks[symbol] = close
    return penny_stocks


if __name__ == "__main__":
    start_time = time.time()
    penny_stocks = find_penny_stocks()
    end_time = time.time()
    print(f"Found {len(penny_stocks)} penny stocks")
    print(penny_stocks)
    print(f"Execution time: {end_time - start_time} seconds")
