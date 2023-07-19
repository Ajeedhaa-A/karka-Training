my_resume={"Name":"aji","E-mail":"ajiji123@gmail.com","Mobile-no":9878654345,
           "Softskills":["Teamwork","Time Management"],"Hardskills":["Typing","Tally","Photoshop","cybersecurity"],
           "Edu_q":[{"edu":"SSLC","institute":"St.Joseph Convent","percentage":93.33},
                    {"edu":"HSC","institute":"St. Joseph convent","percentage":80.033},
                    {"edu":"BSc.CS_Graduate","institute":"Government arts and science","percentage":80}],
           "Project":["early kidney disease prediction","Penetrating testing and vulnerability assesment"],
           "Experience":[{"company name":"TCS","role":"graduate trainee","duration":1,"Place":"Trivandram"},
                         {"company name":"infosys","role":"python developer","duration":2,"Place":"coimbatore"},
                         {"company name":"zoho","role":"full stack developer","duration":4,"Place":"chennai"}],
           "Hobbies":["Reading books","aari work","gardening"],
           "Address":{"father name":"Kalifha","father Occupation":"coolie","Language":["Tamil","English"],"DOB":"21-11-2002",
           "gender":"female","martial status":"single",
           "Add":{"doorno":62,"street":"Rahmath Garden","city":"nagercoil","pincode":629002}}}

resume = my_resume.items()
for i,item in resume:
    #print(i,":",item)
    if type(item)==str:
        print(i,":",item)
    elif type(item)==list:
        print(i,":")
        for o in item:
            print("\t",o)
            if type(o)==dict:
                for h,t in o.items():
                   print("\t\t",h,":",t)
                   
    elif type(item)==dict:
        print(i,":")
        for s,q in item.items():
              if type(q)==str:
                print("\t",s,":",q)
              elif type(q)==list:
                  print("\t",s,":")
                  for u in q:
                      print("\t\t",u)
    
            
              elif type(q)==dict:
                print("\t",s,":")
                for p,y in q.items():
                    print("\t\t",p,":",y)

                #print("\t",s,":",q)
            
        
        
        

    