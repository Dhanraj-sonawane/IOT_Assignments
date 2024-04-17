# 6) Write a Python function to calculate the factorial of a number (a non-negative integer). The function acc
# epts the number as an argument.

num=int(input("enter the number"))

def cal_factorial(num):
    i=1
    fact=1
    while (i<=num):
        fact=fact*i
        i=i+1
    return fact

print(f"factorial of {num} is : {cal_factorial(num)}")