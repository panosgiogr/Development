min_stu_name=""
min_stu_mark=20.1
max_stu_name=""
max_stu_mark=0.0
for i in range(1,27,1):
    stu_name=raw_input("Δώσε όνομα μαθητή : ")
    stu_mo=0
    for i in range(1,11,1):
        stu_mo+=float(input("Δώσε "+str(i)+"ο βαθμό για τον μαθητή : "+stu_name+" :"))
    stu_mo=stu_mo/10
    if stu_mo>max_stu_mark:
        max_stu_mark=stu_mo
        max_stu_name=stu_name
    if stu_mo<min_stu_mark:
        min_stu_mark=stu_mo
        min_stu_name=stu_name
print "Ο μαθητής με το μεγαλύτερο Μ.Ο. είναι ο/η :" ,max_stu_name," με βαθμό ",max_stu_mark
print "Ο μαθητής με το μικρότερο Μ.Ο. είναι ο/η :" ,min_stu_name," με βαθμό ",min_stu_mark
