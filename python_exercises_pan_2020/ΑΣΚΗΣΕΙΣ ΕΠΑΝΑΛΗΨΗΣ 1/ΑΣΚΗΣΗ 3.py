student_name=raw_input("Δώσε ονοματεπώνυμο μαθητή : ")
min_mark=20
min_good_student_name=""
while student_name!=" ":
    mark_1 = int(input("Δώσε 1ο βαθμό : "))
    mark_2 = int(input("Δώσε 2ο βαθμό : "))
    mark_3 = int(input("Δώσε 3ο βαθμό : "))
    mark_4 = int(input("Δώσε 4ο βαθμό : "))
    mark_5 = int(input("Δώσε 5ο βαθμό : "))
    mark_6 = int(input("Δώσε 6ο βαθμό : "))
    mark_7 = int(input("Δώσε 7ο βαθμό : "))
    mark_8 = int(input("Δώσε 8ο βαθμό : "))
    mark_9 = int(input("Δώσε 9ο βαθμό : "))
    mark_10 = int(input("Δώσε 10ο βαθμό : "))
    avg_mark= (mark_1+mark_2+mark_3+mark_4+mark_5+mark_6+mark_7+mark_8+mark_9+mark_10)/10
    print avg_mark,student_name
    if avg_mark<min_mark:
        min_mark=avg_mark
        min_good_student_name=student_name
print "Ο Άριστος μαθητής με το μικρότερο Μ.Ο. είναι ο/η :",min_good_student_name
