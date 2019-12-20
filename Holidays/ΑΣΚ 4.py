min_stu_name=""
min_stu_mark=20.1
max_stu_name=""
max_stu_mark=0
for i in range(1,27,1):
    stu_name=raw_input("Δώσε όνομα μαθητή : ")
    stu_mo=0
    for i in range(1,11,1):
        stu_mo+=float(input("Δώσε "+i+"ο βαθμό για τον μαθητή : "+stu_name+" :"))
    stu_mo=stu_mo/10
    if stu_mo>max_stu_mark:
        max_stu_mark=stu_mo
        max_stu_name=stu_name
    if stu_mo<min_stu_mark:
        min_stu_mark=stu_mo
        min_stu_name=stu_name
print max_stu_name,max_stu_mark
print min_stu_name,min_stu_mark

