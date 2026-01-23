"""
Exception:  An error that are comes at the runtime and they terminate  the recent
code (abnormal termination) . so to prevent them we use exception handling
"""

# put critical code inside the try block
try:
    num1 = int(input("Enter any number: "))
    num2 = int(input("Enter the 2nd number: "))
    
    result = num1 / num2 
    print(result)

except ZeroDivisionError as e:
    print("Invalid user input..", e)

except Exception as e:
    print("invalid data..", e)


finally :
    print("Congratulation code running successful!!")