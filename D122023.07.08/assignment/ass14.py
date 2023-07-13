print("WELCOME TO MITHELL'S TINY ADVENTURE!")
print("You are in a creepy house! Would you like to go \"upstairs\" or into the \"kitchen\" ")
q1=input((">"))
if q1=="kitchen":
    print("There is a long countertop with dirty dishes everywhere. Off to one side \n there is as you'd expect, a refrigerator. You may open the \"refrigerator\" \n or look in a \"cabinet\".")
    q2=input((""))
    if q2=="refrigerator":
        print("Inside the refrigerator you see food and stuff. It looks pretty nasty.\n Would you like to eat some of the food?(\"Yes\" or \"no\") ")
        q3=input((""))
        if q3=="no":
          print("You die of starvation.. eventually. ")  
        else:
           print("You will die") 
    elif q2=="cabinet":
        print("Inside the cabinet you see things, do you take any things from cabinet (\"Yes\" or \"no\") ")

            
    
    