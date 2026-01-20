env = (input("hello user, please Enter the environment :"))
print("The User inout Env is :", env)

if env == "prod" : 
    print("dont't deploy on Friday")

elif env == "steg" :
    print("take backup and test well")

else:
    print("save to deploy any Day")
