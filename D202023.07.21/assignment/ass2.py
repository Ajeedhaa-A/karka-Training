consumer_data={"consumer_name":"user","eb_reading":[1100,1170,1350,1650,2000,2700,4500]}

def cal_bill(consumer_data):
  amount=0
  s=consumer_data['eb_reading']
  for i in range(len(s)-1):
    unit=s[i+1]-s[i]
    print(unit)
    if unit<100:
      amount+=amount
      print(f"month:{i+1}\nunits consumed:{unit}\nbill amount:{amount}")
    elif unit>=100 and unit<=200:
      amount+=2*unit
      #print(amount)
      print(f"month:{i+1}\nunits consumed:{unit}\nbill amount:{2*unit}")
      
  #print(s)
    elif unit>200 and unit<=500:
       amount+=5*unit
       print(f"month:{i+1}\nunits consumed:{unit}\nbill amount:{5*unit}")
    elif unit>500 and unit<=1000:
       amount+=10*unit
       print(f"month:{i+1}\nunits consumed:{unit}\nbill amount:{10*unit}")
       
    elif unit>1000:
       amount+=14*unit
       print(f"month:{i+1}\nunits consumed:{unit}\nbill amount:{14*unit}") 
  
    else:
      print("none")
  print("\n")
  print(f"total amount:{amount}")

cal_bill(consumer_data)

