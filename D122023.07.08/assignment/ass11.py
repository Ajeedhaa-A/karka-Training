weight=int(input("Please enter your current earth weight:"))
print("I have information for the following planets:")
x=int(input("Which planet are you visiting?"))
def planets(x):
    if x==1:
        venux=0.78
        return venux
    elif x==2:
        mars=0.39
        return mars
    elif x==3:
        jupiter=2.65
        return jupiter
    elif x==4:
        saturn=1.17
        return saturn
    elif x==5:
        uranus=1.05
        return uranus
    elif x==6:
        neptune=1.23
        return neptune
    else:
        return 
print(f"Your weight would be {weight*planets(x)} pounds on that planet")
