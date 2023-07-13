print("I will add up the numbers you give me.")
sum=0
for i in range(100):
   num=int(input("Number:"))
   if num==0:
    break
   else:
    sum=sum+num
    print(f"The total so far is{num}")
        
print(f"The total is {sum}")        