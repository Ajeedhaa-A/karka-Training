a=int(input("Enther the value of a "))
b=int(input("Enther the value of a "))
h=int(input("Enther the value of a "))
def traparea(a,b,h):
    area=a+b
    a=area/2
    c=a*h
    return c
print("Area of a trapzium",traparea(a,b,h))