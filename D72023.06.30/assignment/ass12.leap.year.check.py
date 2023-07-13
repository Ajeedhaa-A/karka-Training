yr=int(input("Enter the year:"))
if (((yr%4==0)and (yr/100!=4)) or (yr/400==0)):
    print("leap year is",yr)
else:
    print("not a leap year",yr)