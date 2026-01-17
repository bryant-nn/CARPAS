import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("discountingcashflows_api_key")

def get_data(url):
    response = requests.get(url)
    print(response.status_code, response)
    response.encoding = 'utf-8'
    return json.loads(response.text)

def get_transcript(ticker, quarter, year):
    url = f"https://discountingcashflows.com/api/transcript/{ticker}/{quarter}/{year}/"
    url = f"https://financialmodelingprep.com/api/v3/discounted-cash-flow/{ticker}/{quarter}/{year}"
    transcript = get_data(url)
    if transcript:
        with open(f'./{ticker}_{year}_{quarter}.json', 'w') as f:
            json.dump(transcript[0], f, ensure_ascii=False)

def get_income_statement(ticker):
    url = f"https://discountingcashflows.com/api/income-statement/?ticker={ticker}&period=quarterly&key={api_key}&currency=USD"
    income_statement = get_data(url)
    if income_statement:
        with open(f'Finance/data/income-statement/{ticker}.json', 'w') as f:
            json.dump(income_statement, f, ensure_ascii=False)

def get_balance_sheet_statement(ticker):
    url = f"https://discountingcashflows.com/api/balance-sheet-statement/?ticker={ticker}&period=quarterly&key={api_key}&currency=USD"
    balance_sheet_statement = get_data(url)
    if balance_sheet_statement:
        with open(f'Finance/data/balance-sheet-statement/{ticker}.json', 'w') as f:
            json.dump(balance_sheet_statement, f, ensure_ascii=False)

def get_cash_flow_statement(ticker):
    url = f"https://discountingcashflows.com/api/cash-flow-statement/?ticker={ticker}&period=quarterly&key={api_key}&currency=USD"
    cash_flow_statement = get_data(url)
    if cash_flow_statement:
        with open(f'Finance/data/cash-flow-statement/{ticker}.json', 'w') as f:
            json.dump(cash_flow_statement, f, ensure_ascii=False)

def get_all_data(ticker):
    # get_income_statement(ticker)
    # get_balance_sheet_statement(ticker)
    # get_cash_flow_statement(ticker)
    quarters = ["Q1", "Q2", "Q3", "Q4"]
    years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
    
    for year in years:
        for quarter in quarters:
            if os.path.exists(f'./{ticker}_{year}_{quarter}.json'):
                # print(f"Transcript for {ticker} {quarter} {year} already exists.")
                continue
            else:
                get_transcript(ticker, quarter, year)
    # get_transcript(ticker, "Q1", 2023)

if __name__ == "__main__":
    tickers = ["INTC", "SSNLF", "TSM", "UMC", "GFS"]
    for ticker in tickers:
        get_all_data(ticker)
