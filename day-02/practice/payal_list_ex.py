# list example

# list is the collection of different type of data

#objects = [100, "dog", "raju",27.3,-2, True] # 1st type fo create list
a = list() # 2nd type of create a list 
#print(type(objects)) # print type of list 
#print(objects)
print(type(a))
print(a)
#objects.append("radhe radhe")
#print(objects)
a.append("aws")
a.append("azure")
a.append("GCP")
a.append("IBM")
a.append("allibaba")
a.append("Utho")
print(a)
print (f"lenght of list is : {len(a)}")
print(f"World leader for cloud service provider : {a[0]}")
print(f"Indian cloud service provider is : {a[-1]}")
print(dir(a))
print(a.extend.__doc__)

for cloud in a:
    if cloud == "aws" :
        print(f"World leader for cloud service provider : {cloud}")   
    if cloud == "Utho" :
        print(f"Indean cloud provider is : {cloud}")
    if cloud == "azure" :
        print(f"we learn {cloud} in Josh bash 10 ")
    if cloud == "IBM" or cloud == "allibaba" :
        print(f"{cloud} I don't know about that")