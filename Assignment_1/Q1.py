#1] Write a Python Program find an area of a rectangle and perimeter of the rectangle

le=float(input("enter the lenght"))
be=float(input("enter the breght"))

def area():
    area= le * be
    return area

def perimeter():
    perimeter=2*(le+be)
    return perimeter

print(f"area is : {area()}")

print(f"area is : {perimeter()}")
