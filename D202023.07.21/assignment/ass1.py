item_lst=[{"name":"Apple","category":"Fruits"},{"name":"Carrot","category":"Vegetable"},{"name":"Orange","category":"Fruits"},{"name":"onion","category":"Vegetable"},{"name":"ladyfinger","category":"Vegetable"}]
fruit=[]
veg=[]
varaiety={}
for item in item_lst:
  
   # print(item['name'])
  if item['category']=="Fruits":
        s=item['name']
        fruit.append(s)
       # print(fruit)
  elif item['category']=="Vegetable":
        s=item['name']
        veg.append(s)
       # print(veg)
#s={"Fruits":fruit,"Vegetable":veg}
#print(s)
#print({"Fruits":fruit,"Vegetable":veg})
varaiety["Fruits"]=fruit
varaiety["Vegetables"]=veg
print(varaiety)
