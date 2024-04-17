#   2] Write a program to accept a 4 digit number and
# a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
#    ut should be
# a. 9 3 6 1
# b. 9361 = 9 000 + 300 + 60 + 9
# c. 1639

num=int(input("enter the number"))



temp=num
while (num>0):
    temp=num%10
    print(f"face value of {temp} digit is {temp}")
    num=num//10

print(f"num = {num}")