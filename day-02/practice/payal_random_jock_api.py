import requests
import json

# type of jocks
PJ_jock_url= "https://official-joke-api.appspot.com/random_joke" # jock 1
Dad_jock_url= "https://icanhazdadjoke.com/"  # jock 2

def rendom_jock_api(url_type, mood):  # parameter specifiy the url type
    headers = {
        "Accept" : "Application/json"
    }

    response = requests.get(url= url_type, headers= headers)  # get data
    
    if mood== "PJ":
        data= response.json() # for formate the data
        return data["setup"]+ data["punchline"]   # return to the function
    
    if mood== "Dad":
        data= response.json()
        return data['joke']

mood = input("Which jock would you like to here(Dad, PJ): ")  # ask from user for which type of url 
if (mood == "PJ"): 
    url_type = PJ_jock_url 

else:
    url_type = Dad_jock_url


final_jock = rendom_jock_api(url_type, mood)  # function return some values
print (final_jock)


json_str = json.dumps(final_jock, indent=4)
with open("joke.json", "w") as f:
    f.write(json_str)

f.close()



#with open('data.json', 'w') as json_file:
   # json.dump(data, json_file, indent=4)