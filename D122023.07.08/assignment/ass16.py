x=input("What is your gender(M or F):")
f_name=input("First name:")
l_name=input("Last name:")
y=int(input("Age:"))
print("\n")
if x=="F" and y>=20:
   print(input(f"Are you married .{f_name} (y or n)?"))
   print(f"Then I shall call you Mrs.{l_name}")
elif x=="F" and y<20:
   print("Then I shall call you Ms.{}{}".format(f_name,l_name))
elif x=="M" and y>=20:
    input(f"Are you married .{f_name} (y or n)?")
    print(f"Then I shall call you Mr.{f_name}{l_name}")    
else:
    print(f"Then I shall call you Mr.{f_name}{l_name}")