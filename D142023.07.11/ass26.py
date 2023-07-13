
def  add_keychains():
   return "ADD KEYCHAINS"
def remove_keychains(s):
    return s 
def view_order(s):
    return s
def checkout(s):
    return s
for i in range(15):
    print("ye Olde keychain shoppe")
    print("1.Add Keychains to Order \n 2.Remove Keychains from Order.\n 3.View current Order.\n 4.Checkout\n")
    x=int(input("please enter your choice"))
    if x==4:
        s="checkout"
        print(checkout(s))
        break
    elif x==1:
        #s="ADD keychains"
        print(add_keychains())
        print("\n")
    elif x==2:
        s="Remove Keychains"
        print(remove_keychains(s)) 
        print("\n")
    elif x==3:
        s="view current Order" 
        print(view_order(s))  
        print("\n")
    else:
        print("none")   
        print("\n")
    
    


