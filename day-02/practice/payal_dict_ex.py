# dictionary data structure
# dictionary is a collection of the data with key value paire 

info = {"name":"payal",
        "age": 22,
        "profession": "fresher",
        "Education": "graduation",
        "city" : "Indore",
        "salary" : 22.5,
        "married" : False
        } # 1st type of create dictionary
#fruits = dict() # 2nd type of create dictionary
print(type(info)) 
print(f"I live in {info["city"]}") 
print(f"I am currently a {info['profession']}")
print(f"My age is {info['age']} ")
print("my current salary is", info.get("salary","Not found"))

info.update({"age": 23})
#print(dir(info)) # give the all attributes and methods of object
print(info.items.__doc__)

# this is Iterate for dictionary 
for value in info.items():
    print(value)