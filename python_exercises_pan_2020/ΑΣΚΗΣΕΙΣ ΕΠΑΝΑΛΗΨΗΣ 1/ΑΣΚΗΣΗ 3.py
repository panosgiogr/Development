student_name=raw_input("Δώσε ονοματεπώνυμο μαθητή : ")
min_mark=10000
sum_mark=0
min_good_student_name=""
while student_name!=" ":
    for i in range(1,11,1):
        mark = int(input("Δώσε τον "+str(i)+"ο βαθμό : "))
        sum_mark=sum_mark+mark
    avg_mark= float(sum_mark / 10)
    print avg_mark,student_name
    if avg_mark>=18 and avg_mark<min_mark:
        min_mark=avg_mark
        min_good_student_name=student_name
    student_name=raw_input("Δώσε ονοματεπώνυμο μαθητή : ")
print "Ο Άριστος μαθητής με το μικρότερο Μ.Ο. είναι ο/η :",min_good_student_name