#author panosgio
man_with_max_kids_name=""
man_with_max_kids_count=0
women=0
women_kids=0
for i in range(1,21,1):
    name=raw_input("Δώσε όνομα υπάλληλου : ")
    gender=raw_input("Δώσε φύλο "+name)
    if name!="Άνδρας" or name!="Γυναίκα":
        gender = raw_input("Δώσε φύλο " + name)
    kids=int(input("Δώσε αριθμό παιδιών για τον/την : "+name))
    if kids<0:
        kids = int(input("Δώσε αριθμό παιδιών για τον/την : " + name))
    if kids>man_with_max_kids_count and gender=="Άνδρας":
        man_with_max_kids_count=kids
        man_with_max_kids_name=name
    if gender=="Γυναίκα":
        women=+1
        women_kids=+kids
print "Ο άνδρας με τα περισσότερα παιδιά είναι ο",man_with_max_kids_name
print "Ο Μ.Ο. παιδιών των γυναικών στην εταιρία είναι :",women_kids/women

