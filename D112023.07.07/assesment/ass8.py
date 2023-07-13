name=input("Hey, What's your name?")
print("\n")
age=int(input(f"OK, {name}, how old are you?"))
print("\n")
if age<=16:
    print(f"You can't drive, {name}")
if age<18:
    print(f"You can't vote ,{name}.")
if age<25:
    print(f"You can't rent a car,{name}")
if age>=25:
    print("You can do anything that's legal")            