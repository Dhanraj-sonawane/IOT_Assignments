# 5)The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
# ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

num1 = float(input("Enter num1 : "))
num2 = float(input("Enter num2 : "))
num3 = float(input("Enter num2 : "))

def cal_avg(num1,num2,num3):
    avg=((num1+num2+num3)/3)
    return avg

def disply_grade(avg):
    if (avg >=90 and avg<=100):
        print("grade A")
    elif (avg >= 80 and avg <= 89):
        print("grade B")
    elif (avg >= 70 and avg <= 79):
        print("grade c")
    elif (avg >= 60 and avg <= 69):
        print("grade D")
    elif (avg>=60 and avg <= 69):
        print("grade E")

disply_grade(cal_avg(num1,num2,num3))

