import json
consumer_data={"consumer_name":"user","eb_reading":[1100,1170,1350,1650,2000,2700,4500]}
def cal_bill(consumer_data):
  amount=0
  ls=[]
 
  s=consumer_data["eb_reading"]
  for i in range(len(s)-1):
    #print(i)
    dicss={}
    unit=s[i+1]-s[i]
    #print(unit)
    if unit<100:
      amount=amount
    elif unit>=100 and unit<=200:
      amount=2*unit
    elif unit>200 and unit<=500:
       amount=5*unit
    elif unit>500 and unit<=1000:
       amount=10*unit      
    elif unit>1000:
       amount=14*unit
    else:
      print("none")

    dicss["month"]=i+1
    dicss["unit"]=unit
    dicss["amount"]=amount
    #print(dicss)
    ls.append(dicss)
    #print(ls)
  #string = str(ls)
  #print(type(string))
  return ls
#print(cal_bill(consumer_data))
aj=cal_bill(consumer_data)
#print(aj)
str_list=str(aj)
#print(str_list)
#print(type(str_list))
file=open("/home/codeji/karka/D222023.07.22/practice/aji.txt",'w')
file.write(str_list)
file.close()
choice=input("How to save your file dict or json?")
if choice.upper()=="DICT":
    file=open("/home/codeji/karka/D222023.07.22/practice/aji.txt",'w')
    file.write(str_list)
    file.close()
     #print(aj)
elif choice.upper()=="JSON":
     file=open("/home/codeji/karka/D222023.07.22/practice/aji.txt",'w')
     file.write(json.dumps(str_list))
     file.close()
    #print(json.dumps(str_list))