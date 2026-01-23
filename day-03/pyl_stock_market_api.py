import requests

def stock_market_api_data():
    Key= "6ORZYSFIS3NLT5QT" # key for api call
    symbole= "IBM"
    server_url= "https://www.alphavantage.co/" # host url for api call
    stock_api_url=f"query?function=TIME_SERIES_DAILY&symbol={symbole}&apikey={Key}" # entire api call url

    #print(server_url+stock_api_url) # api url
    try :
        response = requests.get(url= server_url+stock_api_url) # client api request for get data
        status_code= response.status_code
        if status_code == 200 :
            print(f"The status code for api : {status_code}")
            data= response.json() # for get formated json data
            for key,value in data.items():
                if key == 'Meta Data' :
                    print(key,value)
                else: 
                    continue
    except requests.exceptions.RequestException as e:
        print("Network error" , e) 



stock_market_api_data()
