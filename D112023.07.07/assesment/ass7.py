height=float(input("Your height in m:"))
weight=int(input("Your weight in kg:"))
#print("\n")
#print("Your BMI is",weight/height**2)
def bmi(height,weight):
    return weight/height**2
print("Your BMIis",bmi(height,weight))