#author panosgio
competitors_mark_over_18=0
max_mark=0
for i in range(30):
    mark_1 = int(input("Δώσε 1ο βαθμό : "))
    mark_2 = int(input("Δώσε 2ο βαθμό : "))
    mark_3 = int(input("Δώσε 3ο βαθμό : "))
    max_mark=mark_1
    if mark_2>max_mark:
        max_mark=mark_2
    if mark_3>max_mark:
        max_mark=mark_3
    print "Ο μεγαλύτερος βαθμός είναι :",max_mark
    if max_mark>=18:
        competitors_mark_over_18+=1
print "Το πλήθος των υποψήφιων με βαθμό μεγαλύτερο ή ίσο του 18 είναι :",competitors_mark_over_18