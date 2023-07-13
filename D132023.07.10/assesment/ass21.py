height=float(input("Your height in m:"))
weight=int(input("Your weight in kg:"))
print("\n")
BMI=weight/height**2
print(f"Your BMI is {BMI}")
if BMI<=18.5:
    print("BMI Category:under weight")
elif BMI>18.5 and BMI<=24.9: 
    print("BMI Category:normal weight")
elif BMI>25.0 and BMI<=29.9:
    print("BMI Category:Overweight")
else:
    print("obese")  