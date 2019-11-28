student_first_score=""
student_first_score_test_count=10000
for i in range(1,31,1):
    student_name=raw_input("Δώσε ονοματεπώνυμο μαθητή : ")
    score=0
    test_count=0
    while score<50:
        test_count+=1
        test_mark = int(input("Δώσε βαθμό για το "+test_count+"ο τεστ : "))
        score=+test_mark
    if test_count<student_first_score_test_count:
        student_first_score_test_coun=test_count
        student_first_score=student_name
print "Ο μαθητής με το μικρότερο αριθμό τεστ που να συμπληρώσει τους 50 βαθμούς είναι ο/η :",student_first_score

