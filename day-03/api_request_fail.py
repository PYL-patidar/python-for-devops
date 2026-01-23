import requests

def api_call():
    try: 
        api_url = input("Enter your api-url for api request: ")

        response = requests.get(url= api_url)

        if response.status_code == 200 :
            try:
                print(response.json())
            except ValueError as e:
                print("Response is not in Json: ", e)
                print(response.text)
        else:
            print("api request failed")


    except Exception as e :
        print("something error : ", e)
api_call()
