import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_CONNECTION_NAME = os.getenv('DB_CONNECTION_NAME')

def get_db_connection():
    return mysql.connector.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        host='34.170.32.126'
    )

def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_data (
            ticker VARCHAR(10),
            open_price FLOAT,
            low_price FLOAT,
            high_price FLOAT,
            volume BIGINT,
            date DATE,
            date_pulled TIMESTAMP,
            PRIMARY KEY (ticker, date)
        )
    ''')
    connection.commit()
    cursor.close()
    connection.close()

def get_latest_date(ticker):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT MAX(date) FROM stock_data WHERE ticker = %s', (ticker,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0]

def upsert_stock_data(ticker, data):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    for date, price_info in data.items():
        open_price = float(price_info['1. open'])
        low_price = float(price_info['3. low'])
        high_price = float(price_info['2. high'])
        volume = int(price_info['5. volume'])
        date_pulled = datetime.now()
        
        cursor.execute('''
            INSERT INTO stock_data (ticker, open_price, low_price, high_price, volume, date, date_pulled)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                open_price = VALUES(open_price),
                low_price = VALUES(low_price),
                high_price = VALUES(high_price),
                volume = VALUES(volume),
                date_pulled = VALUES(date_pulled)
        ''', (ticker, open_price, low_price, high_price, volume, date, date_pulled))
    
    connection.commit()
    cursor.close()
    connection.close()

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

def get_historical_data(symbol, from_date=None):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'outputsize': 'full',
        'apikey': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    if 'Error Message' in data:
        print(f"Error fetching data for {symbol}: {data['Error Message']}")
        return None

    time_series = data.get('Time Series (Daily)', {})
    if from_date:
        filtered_data = {date: value for date, value in time_series.items() if date > from_date}
        return filtered_data
    else:
        return time_series

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
    create_table()

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
            latest_date = get_latest_date(symbol)
            if latest_date:
                from_date = latest_date.strftime('%Y-%m-%d')
                data = get_historical_data(symbol, from_date)
            else:
                data = get_historical_data(symbol)

            if data:
                print(f"Inserting/updating data for {symbol}...")
                upsert_stock_data(symbol, data)
                print(f"Data for {symbol} has been inserted/updated.")

                while True:
                    query_date = input("Enter a date to query (YYYY-MM-DD) or 'exit' to quit: ").strip()
                    if query_date.lower() == 'exit':
                        break
                    
                    try:
                        datetime.strptime(query_date, '%Y-%m-%d')
                        price_on_date = get_stock_price_on_date(data, query_date)
                        if price_on_date:
                            print(f"\nPrice data for {symbol} on {query_date}:")
                            print(json.dumps(price_on_date, indent=2))
                        else:
                            print(f"No data available for {query_date}")
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

        else:
            print("Invalid choice. Please enter '1', '2', or 'exit'.")