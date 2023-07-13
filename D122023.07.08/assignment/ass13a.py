print("TWO QUESTIONS!")
print("Think of an object,and I'll try to guess it.")
print("Qusetion 1) Is it animal, vegetable, or mineral?")
q1=input(">")
if q1=="animal":
    print("Quesion 2) Is it bigger than a breadbox")
    q2=input(">")
    if q2=="yes":
      print("My guess is that you are thinking of a mouse.\n I would ask you if I'm right, but I don't actually care")
if q1=="animal":
    if q2=="no":
       print("My guess is that you are thinking of a squirrel.\n I would ask you if I'm right, but I don't actually care")
if q1=="vegetable":
    print("Quesion 2) Is it bigger than a breadbox")
    q2=input(">")
    if q2=="yes":
       print("My guess is that you are thinking of a watermelon.\n I would ask you if I'm right, but I don't actually care")    
if q1=="vegetable":
    if q2=="no":
        print("My guess is that you are thinking of a carrot.\n I would ask you if I'm right, but I don't actually care")
if q1=="mineral":
    print("Quesion 2) Is it bigger than a breadbox")
    q2=input(">") 
    if q2=="yes":
        print("My guess is that you are thinking of a camero.\n I would ask you if I'm right, but I don't actually care")    
if q1=="mineral":
    if q2=="no":
      print("My guess is that you are thinking of a paper clip.\n I would ask you if I'm right, but I don't actually care")  
else:
    print("none")      