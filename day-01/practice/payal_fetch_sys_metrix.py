import psutil

print("--CPU Usage--")
print (psutil.cpu_percent(interval=1))

print("--Memory Usage--")
print(psutil.virtual_memory)

print("--Disk Usage--")
print(psutil.disk_usage)

print("--Network state--")
print(psutil.net_io_counters)