l1=[]
cur="INR"
for i in range(4):
     app=(input("Enter the list value"))
     l1.append(app)
print(l1)     
l2=[]
for item in l1:
         l2.append(cur+str(item))
print(l2)
