item1=int(input("Enter the amount of item1"))
item2=int(input("Enter the amount of item2"))
item3=int(input("Enter the amount of item3"))
item4=int(input("Enter the amount of item4"))
total=item1+item2+item3+item4
print("Total amount:$",total)
if ((total>=500) and (total<1000)):
    print("You have owned a a silver token")
#elif total>1000:
    print("You have owned a golded token")
elif ((total<=1000) and (total>2000)):
    print("You have owned a platinum token")
else:
    print("thanks for purchasing, come again")