Education_details=[{"study":"B.tech","Institute":"cape","Semester":[{"semester":1,
                "Sub":["computer science","Maths","Data Science", "Machine Learning"],"semester_grade":"A"}]},
                {"study":"B.tech","Institute":"cape","Semester":[{"semester":2,
                "Sub":["data communication","pyhon lab","Computer archietecure", "Os"],"semester_grade":"O"}]}]
for item in Education_details:
    print(item['Semester'])
    sems=item['Semester']
    for s in sems:
       print(s['Sub'])
       ss=s['Sub']
       for y in ss:
           print(y)