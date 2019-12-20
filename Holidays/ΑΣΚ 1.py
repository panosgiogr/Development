max_mark=0
mark=float(input("Δώσε βαθμό μαθητή : "))
while mark>0:
    if mark>=9.5:
        print "ΠΕΡΑΣΕΣ"
    else:
        print "ΑΠΕΤΥΧΕΣ"
    if mark>max_mark:
        max_mark=mark
    mark = float(input("Δώσε βαθμό μαθητή : "))
print "Ο μεγαλύτερος βαθμός στη τάξη είναι :",max_mark