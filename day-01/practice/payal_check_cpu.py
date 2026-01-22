import psutil 

# apko kamm krna hai ki User se CPU thresold lena hai 
# then current cpu usage pata krna hai 
# agar cpu usage threshold se jyada hua, to send email.

def get_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU Threshold: "))

    current_cpu_state = psutil.cpu_percent(interval=1)
    print(f"Current CPU state is : {current_cpu_state}")

    if current_cpu_state > cpu_threshold:

        print(f"Please check your email, your cpu usage is out of threshold limits.")
    else:
        print ("CPU in the safe state...")

get_cpu_threshold()