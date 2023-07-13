quiz=(input("Are you ready for a quiz?"))
count=0
if quiz=="Y"or quiz=="y":
  print("Okay, here it comes!\n")
  print("Q1) What is the capital of Alaska?\n \t 1) Melbourne \n\t 2) Anchorage \n\t 3) Juneau")
  q1=int(input(""))
  if q1==3:
        print("That's right!")
        count+=1
  else:
        print("sorry,its not correct")   
        print("Q2) Can you store the value \"cat\" in a variable of type int? \n\t 1)yes \n\t 2)no")    
  q2=int(input())
  if q2==1:
    print("Sorry, \" cat\" is a string. ints can only store numbers. ")
  else:
    print("That's right!")  
    count+=1 

    print("Q3) What is the result of 946/3?\n\t 1) 5\n\t 2) 11 \n\t 3)15/3") 
  q3=int(input())
  if q3==2:
    print("That's correct!")
    count+=1
  else:
        print("Sorry,its not correct!")    
        print("\n\n")
        print(f"Overall, you got {count} out of 3 correct.")
        print("Thanks for playing!")
else:
   print("its ok") 

  
