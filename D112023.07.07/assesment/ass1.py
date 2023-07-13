#print("+"+"-"*63+"+")
#sub="English III"
#trs="Ms. Lapan"
#pre="Precalculus"
#goe="Mrs. Gideon"
#mus="Music Theory"
#dav="Mr. Davis"
#bio="Biotechnology"
#pal="Ms.  Palmer"
#pri="Principles of Technology I"
#Grac="Ms.  Garcia"
#lati="Latin II"
#Barn="Mrs. Barnett"
#Apus="AP US History"
#John="Ms. Johannessen"
#Buss="Bussiness Computer Information Systems"
#Jam="Mr. James"
#print("| 1 |{:>38}|{:>20}|".format(sub,trs))
#print("| 2 |{:>38}|{:>20}|".format(pre,goe))
#print("| 3 |{:>38}|{:>20}|".format(mus,dav))
#print("| 4 |{:>38}|{:>20}|".format(bio,pal))
#print("| 5 |{:>38}|{:>20}|".format(pri,Grac))
#print("| 6 |{:>38}|{:>20}|".format(lati,Barn))
#print("| 7 |{:>38}|{:>20}|".format(Apus,John))
#print("| 8 |{:>38}|{:>20}|".format(Buss,Jam))
#print("+"+"-"*63+"+")
subjects=["English III","Precalculus","Music Theory","Biotechnology","Principles of Technology I","Latin II","AP US History","Business Computer Information Systems"]
names=["Ms. Lapan","Mrs. Gideon","Mr. Davis","Ms. Palmer","Ms. Garcia","Mrs. Barnett","Ms.  Johannessen","Mr. James"]
bottom="+"+"-"*63+"+"
print(bottom)
for i in range(len(subjects)):

    print("|{}|{:>38}|{:>22}|".format(i+1,subjects[i],names[i]))
print(bottom)