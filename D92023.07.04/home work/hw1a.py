numbers=[7,8,9,1,3,2,10,4,2,5,6]
oddcount=0
evencount=0
for i in numbers:
    if  i%2==0:
       evencount+=1
    else:
       oddcount+=1
print("number of odd numbers",oddcount)
print("number of even numbers",evencount)  