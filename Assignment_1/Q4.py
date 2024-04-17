#4] Write a Python function to find the maximum of three numbers.


num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num2 : "))

if (num1>num2):
        if(num1>num3):
            print("num1 is greater ")
        else:
            print("num3 is greater ")
else:
        if(num2>num3):
            print("num2 is greater ")
        else:
            print("num3 is greater ")