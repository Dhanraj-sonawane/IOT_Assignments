#3] Write a program to accept three integer numbers and find its average.

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num2 : "))

def avarge():
    avg=(num1+num2+num3)/2
    return avg

print(f"avg of numbers is : {avarge():}")