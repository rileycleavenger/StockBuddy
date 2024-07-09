import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')


def search_symbol(keyword):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'SYMBOL_SEARCH',
        'keywords': keyword,
        'apikey': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()


    if 'Error Message' in data:
        print(f"Error searching for {keyword}: {data['Error Message']}")
        return None
   
    return data


def get_historical_data(symbol, outputsize='compact'):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'outputsize': outputsize,
        'apikey': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()


    if 'Error Message' in data:
        print(f"Error fetching data for {symbol}: {data['Error Message']}")
        return None
   
    return data


def print_historical_data(data):
    if not data:
        return


    time_series = data['Time Series (Daily)']
    for date, price_info in time_series.items():
        print(f"Date: {date}")
        for key, value in price_info.items():
            print(f"  {key}: {value}")
        print()


def get_stock_price_on_date(data, date):
    if not data:
        return None


    time_series = data['Time Series (Daily)']
    if date in time_series:
        return time_series[date]
    else:
        return None


if __name__ == '__main__':
    while True:
        choice = input("Enter '1' to search for a stock symbol, '2' to get historical data, or 'exit' to quit: ").strip()
       
        if choice == 'exit':
            break
       
        if choice == '1':
            keyword = input("Enter a keyword to search for stock symbols: ").strip()
            search_results = search_symbol(keyword)
            if search_results and 'bestMatches' in search_results:
                print("Search results:")
                for match in search_results['bestMatches']:
                    print(json.dumps(match, indent=2))
            else:
                print("No results found.")
       
        elif choice == '2':
            symbol = input("Enter the stock symbol (e.g., AAPL): ").strip()
            outputsize = input("Enter the output size (compact/full): ").strip()


            data = get_historical_data(symbol, outputsize)
           
            if data:
                print("Printing all historical data:")
                print_historical_data(data)


                while True:
                    query_date = input("Enter a date to query (YYYY-MM-DD) or 'exit' to quit: ").strip()
                    if query_date.lower() == 'exit':
                        break
                   
                    price_on_date = get_stock_price_on_date(data, query_date)
                    if price_on_date:
                        print(f"\nPrice data for {symbol} on {query_date}:")
                        print(json.dumps(price_on_date, indent=2))
                    else:
                        print(f"No data available for {query_date}")
        else:
            print("Invalid choice. Please enter '1', '2', or 'exit'.")
