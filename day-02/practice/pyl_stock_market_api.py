import requests


def stock_market_api_data():
    Key= "6ORZYSFIS3NLT5QT" # key for api call
    symbole= "IBM"
    server_url= "https://www.alphavantage.co/" # host url for api call
    stock_api_url=f"query?function=TIME_SERIES_DAILY&symbol={symbole}&apikey={Key}" # entire api call url

    print(server_url+stock_api_url) # api url

    response = requests.get(url= server_url+stock_api_url) # client api request for get data
    data= response.json() # for get formated json data
    #print(type(data))
    #print(data)

    # for get specific data
    for key,value in data.items():
        if is_time_series:
            if key == 'Time Series (Daily)':
                continue
            else:
                print(key,value)

data= input("Enter the data which you want to get : ")
is_time_series= True
stock_market_api_data()
