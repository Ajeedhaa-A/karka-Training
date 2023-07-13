passoutyear= int(input("Enter the year"))

def is_eligible(passoutyear):

    return(passoutyear>=2021)
    
if is_eligible(passoutyear):
    print( "eligible")
else:
    print("not eligible")
