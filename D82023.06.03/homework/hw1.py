firstnum=int(input("Enter the first number="))
operator=input("Enter the operator=")
thirdnum=int(input("Enter the third number="))

def calculate(first,operator,third):
    if operator =="+":
      return first+third
    elif operator =="-":
      return first-third
    elif operator =="*":
      return first*third
    elif operator =="/":
       return first/third
    elif operator=="%":
       return first%third
    else:
       print("not supported ,please type the correct operator")
print("answer",calculate(firstnum,operator,thirdnum))