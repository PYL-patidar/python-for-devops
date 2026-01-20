import os
import sys
import datetime


print(os.getcwd()) # shows current working directory
print(os.listdir()) # it list the files into the current directory
#os.mkdir("logs")  # create a dir with name of logs 
#os.makedirs("app/logs", exist_ok=True) # create multiple folders
#os.remove("test.txt") # remove file
#os.rmdir("app") # remove dir

# we have to remembers
# getcwd(), listdir() mkdir() / makedirs(), remove(), rename(), path.exists(),  path.join() environ

#env = sys.argv[1]
#print(f"Deploying to {env}")
#print(sys.path)
#print(sys.version)
print(sys.platform)
#sys.exit("Error occurred")
# sys.argv, sys.exit(), sys.path, sys.version