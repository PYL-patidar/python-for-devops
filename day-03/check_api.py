import requests

try: 
    api_url = input(" Enter the API url : ")
    def check_api_works():
        headers = {
            "Accept" : "Application/json"
        }
        response = requests.get(url= api_url, headers= headers)
        
        if response.status_code >= 400 and response.status_code <= 429 :
            print(response.status_code)
            print("Client side error")
 
        for key,values in response.json().items(): 
            if key == "info" : 
                print(key, values)


except requests.exceptions.RequestException as e : 
    print("invalid api call")

check_api_works()