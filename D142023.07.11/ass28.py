keychain=0
k_price=10
sales_tax=8.25
shipping_cost=5
keychain_cost=1
subtotal=0
total=0
def add_keychains():
     
     add=int(input("You have 0 keychains. How may to add? "))
     print("\n")
     global keychain
     keychain=keychain+add
     print(f"You now have {keychain} keychains. ")
def remove_keychains():
    global keychain
    remv=int(input("You have 3 keychains. How many to remove?"))  
    print("\n") 
    keychain-=remv  
    print(f"You now have {keychain} keychains. ")
def view_order():
         global keychain
         global k_price
         global sales_tax
         global shipping_cost
         global keychain_cost
         global subtotal
         global total
         shipping_cost=5+(1*keychain)
         subtotal=keychain*k_price
         total=subtotal*(sales_tax/100)

         print(f"You now have {keychain} keychains. ") 
         print(f"k_chains cost $10 each.")
         k_price=keychain*10
         #print(f"Total cost is {k_price}")
         print(f"Total cost is {subtotal+total+shipping_cost}")

def checkout():
     global keychain
     global k_price
     print("CHECKOUT")
     print("\n")
     name=input("What is your name? ")
     print(f"You now have {keychain} keychains. ") 
     print(f"k_chains cost $10 each.")
     k_price=keychain*10
     print(f"Total cost is  {subtotal+total+shipping_cost}")
     print(f"Thanks for your order, {name}")
for i in range(15):
    print("\n")
    print("ye Olde keychain shoppe")
    print("1.Add Keychains to Order \n 2.Remove Keychains from Order.\n 3.View current Order.\n 4.Checkout\n")
    x=int(input("please enter your choice"))
    if x==4:
        checkout()
        break
    elif x==1:
       add_keychains()
    elif x==2:
        remove_keychains() 
        print("\n")
    elif x==3:
        view_order() 
        print("\n")
    else:
        print("none")   
        print("\n")
    