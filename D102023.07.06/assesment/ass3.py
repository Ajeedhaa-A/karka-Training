marks=[96,72,80,67,82]
total_marks=0
enum_marks=enumerate(marks)
print(type(enum_marks))
for i,mark in enum_marks:
   print("before iteration process"+str(i))
   print("before sum",total_marks)
   total_marks=total_marks+mark
   print("after sum",total_marks)
   print("After iteration process"+str(i))
   print("\n")