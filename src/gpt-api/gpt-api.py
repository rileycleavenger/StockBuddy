from openai import OpenAI
from typing import List, Tuple, Dict
import scraper
import StockSearch
from StockSearch import search_symbol, get_historical_data
from scraper import extractHeadlines, extractCompanies

client = OpenAI()

class StockAnalysisResult:
    def __init__(self, headlines: List[Tuple[str, str]], gainers: List[Tuple[str, str, str, str]], losers: List[Tuple[str, str, str, str]], stock_data: Dict):
        self.headlines = headlines
        self.gainers = gainers
        self.losers = losers
        self.stock_data = stock_data

    def __repr__(self):
        return f"StockAnalysisResult(headlines={self.headlines}, gainers={self.gainers}, losers={self.losers}, stock_data={self.stock_data})"

def create_prompt(headlines: List[Tuple[str, str]], gainers: List[Tuple[str, str, str, str]], losers: List[Tuple[str, str, str, str]], stock_data: Dict, user_filters: Dict) -> str:
    prompt = "Stock Market Analysis:\n\n"
    prompt += "Today's Headlines:\n"
    for title, link in headlines:
        prompt += f"- {title} ({link})\n"

    prompt += "\nTop Gainers:\n"
    for name, symbol, percent, price in gainers:
        prompt += f"- {name} ({symbol}): {percent}% at ${price}\n"

    prompt += "\nTop Losers:\n"
    for name, symbol, percent, price in losers:
        prompt += f"- {name} ({symbol}): {percent}% at ${price}\n"

    prompt += "\nStock Data:\n"
    for symbol, data in stock_data.items():
        prompt += f"{symbol}:\n"
        for date, price_info in data.items():
            prompt += f"  {date}:\n"
            for key, value in price_info.items():
                prompt += f"    {key}: {value}\n"

    prompt += "\nUser Filters:\n"
    for key, value in user_filters.items():
        prompt += f"- {key}: {value}\n"

    return prompt

def get_gpt_response(prompt: str) -> str:
    response = client.chat.completions.create  (
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def main(user_filters: Dict):
    headlines = extractHeadlines(scraper.news_url)
    gainers = extractCompanies(scraper.gainers_url)
    losers = extractCompanies(scraper.losers_url)

    stock_data = {}
    for filter in user_filters.get('symbols', []):
        data = get_historical_data(filter, outputsize='compact')
        if data and 'Time Series (Daily)' in data:
            stock_data[filter] = data['Time Series (Daily)']

    result = StockAnalysisResult(headlines, gainers, losers, stock_data)
    prompt = create_prompt(result.headlines, result.gainers, result.losers, result.stock_data, user_filters)
    gpt_response = get_gpt_response(prompt)
    print(gpt_response)

if __name__ == "__main__":
    user_filters = {
        'symbols': ['AAPL', 'TSLA'],  # Example symbols
        # Add more filters as needed
    }
    main(user_filters)