s=int(input("Enter the semi-perimeter  of a triangle"))
a=int(input("Enter the  length of a triangle"))
b=int(input("Enter the  of length of side b of a triangle"))
c=int(input("Enter the  of length of side c a triangle"))
def triarea(s,a,b,c):
    triangle=s*(s-a)*(s-b)*(s-c)
    trarea=triangle**(1/2)
    return trarea
print("The area of a triangle",triarea(s,a,b,c))