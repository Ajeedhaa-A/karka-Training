stud_details=[{"name": "abinaya","place":"vattavali",
            "Hobbies":["1.watching series", "2.embroidary", "3.mobiles"], 
            "marks":{"Tamil":98,"English":81,"Maths":98,"Science":92,"Social":76}},
              {"name":"dinesh","place":"vattavilai",
             "Hobbies":["1.criket ","2.football","3.volleyball"],
             "marks":{"Tamil":99,"English":82,"Maths":99,"Science":97,"Social":79}},
              {"name":"abineash","place":"peruvilai",
               "Hobbies":["1.criket"," 2.chess", "3.volleyball"],
               "marks":{"Tamil":94,"English":84,"Maths":73,"Science":99,"Social":88}},
              {"name":"ajeedhaa","place":"kannankulam",
               "Hobbies":["1.Aari work"," 2.Gardening", "3.Reading Books"],
               "marks":{"Tamil":95,"English":82,"Maths":83,"Science":91,"Social":82}},
              {"name":"sri_ram","place":"krishnankovil",
               "Hobbies":["1.criket" , "2.chess", "3.carom"],
                 "marks":{"Tamil":70,"English":85,"Maths":99,"Science":69,"Social":59}}]
for stud in stud_details:
    total=0
    s=stud['marks']
    print(s)
    for i in s:
       
        mark=stud['marks'][i]
        total+=mark
    print(total)
    per=total/500*100
    print(per)