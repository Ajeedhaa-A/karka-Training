name=input("Hey, What's your name?(Sorry, I keep forgetting)")
age=int(input(f"OK, {name}, how old are you?"))
print("\n")
if age<16:
    print(f"You can't drive,{name}.")
elif age>=16 and age<=17:
    print(f"You can drive but not vote,{name}")
elif age>=18 and age<25:
    print(f"You can vote but not rent a car.{name}")
else:
    print("You can do anything that's legal")            
