x=int(input())
def wday(x):
    if x==1:
        s="Sunday"
        return s
    elif x==2:
        s="Monday"
        return s
    elif x==3:
        s="Tuesday"
        return s
    elif x==4:
        s="wednesday"
        return s
    elif x==5:
        s="thursday"
        return s
    elif x==6:
        s="Friday"
        return s
    elif x==7:
        s="Saturday"
        return s
    elif x==0:
        s="Saturday"
        return s
    else:
        s="error"
        return s
print(f"Weekday {x}:{wday(x)}")    
print("Today is a {}!".format(wday(x)))
