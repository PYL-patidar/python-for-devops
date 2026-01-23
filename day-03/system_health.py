import psutil

# print(dir(psutil)) # get the detail info about python psutil library

configuration = input("Enter what is want to know about the system (CPU, Memory, Disk, Network) : ")

def system_config():
    if configuration == "CPU" :
        print("--CPU Usage--")
        print(psutil.cpu_times())  # used for produce CPU time 
        print(psutil.cpu_percent()) # used for know cpu usage in percentage
        print(psutil.cpu_stats()) # used for know the state of cpu 
        print(psutil.cpu_freq()) # used for know the frequncy
        print(psutil.cpu_count()) # to get for cpu count

    elif configuration == "Memory" :
        print("--Memory Usage--")
        print(psutil.virtual_memory()) # get to know the free, total, used memory 
        print(psutil.swap_memory()) 

    elif configuration == "Disk" :
        print("--Disk Usage--")
        print(psutil.disk_usage("/")) # give disk usage 
        print(psutil.disk_io_counters()) # disk input-output counter, read count, write count etc..
        print(psutil.disk_partitions()) # returns all the partitions of disk

    elif configuration == "Network" :
        print("--Network state--")
        print(psutil.net_io_counters()) # give info about number of byte-send , receive ..
        print(psutil.net_connections()) # connection sockets
        print(psutil.net_if_stats()) 

    else: 
        print("invalid data")

system_config()