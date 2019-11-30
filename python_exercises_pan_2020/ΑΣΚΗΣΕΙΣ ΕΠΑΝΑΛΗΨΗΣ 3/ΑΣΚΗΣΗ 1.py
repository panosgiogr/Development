num=[12,0,14,-52,14,52,-5145,4521,6,1]
#num=[]
#for i in range(1,11,1):
#    x=input("Δώσε "+i+"ο αριθμό : ")
#    num.append(x)
min_num=num[0]
min_num_count=0
for i in range(10):
    if num[i]<min_num:
        min_num=num[i]
        min_num_count=+1
    if num[i]==min_num:
        min_num_count=+1
print "Ο μικρότερος αριθμός είναι ο :",min_num
print "Το",min_num," υπάρχει",min_num_count," φορές στη λίστα"