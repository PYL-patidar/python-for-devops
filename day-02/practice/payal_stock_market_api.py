import requests

API_KEY= "6ORZYSFIS3NLT5QT" # find a API-Key

api_url= "https://www.alphavantage.co/" # then get the base url

symbol= input("Enter the compony name which you want to get stock market(AMZN, GOGE, IBM etc..)")

#interval = 5

query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

print(api_url+query)

def stock_market_data():
    response= requests.get(url=api_url+query)
    print(response.json())


stock_market_data()