# 7) Using for loop, write and run a Python program to find factorial from 0 to
# 10

num=int(input("enter the number"))

def factorials(num):
    for value in range(0,num):
        cal_factorial(value)


def cal_factorial(value):
    i=1
    fact=1
    while (i<=value):
        fact=fact*i
        i=i+1
    print(f"factorial of {value} is {fact}")


factorials(num)
