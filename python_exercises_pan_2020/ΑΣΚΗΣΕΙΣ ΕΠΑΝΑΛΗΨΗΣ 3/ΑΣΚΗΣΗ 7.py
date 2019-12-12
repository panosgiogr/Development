Name=[]
Clss=[]
Mesos=[]
max_vathmos=0
max_vathmos_student=""
for i in range(1,501,1):
    name_input = raw_input("Δώσε ονοματεπώνυμο μαθητή : ")
    clss_input = raw_input("Δώσε τάξη " + name_input + " (Α,Β,Γ) : ")
    Name.append(name_input)
    Clss.append(clss_input)
    mo=0
    for i in range(1,4,1):
        mo_input=int(input("Δώσε βαθμό για "+str(i)+"ο γραπτό : "))
        mo=mo+mo_input
    mo=mo/3
    if clss_input=="Γ" and mo>max_vathmos :
        max_vathmos=mo
        max_vathmos_student=name_input
print "Ο μαθητής με το μεγαλύτερο Μ.Ο. στη Γ΄ τάξη είναι ο/η :",max_vathmos_student
