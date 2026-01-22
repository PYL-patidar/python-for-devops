import requests

url= "https://jsonplaceholder.typicode.com/todos/1" # this is my api url

response = requests.get(url=url) #send client api request and get response
data = response.json()  # convert the response into a sutable json format(javascript object notation)
#print(data)

for key,value in data.items() :
    if key=="userId":
        if value in [1,2,3,4]:
            print("User found")
        else: 
            print("User not found")
