number=int(input("Δώσε έναν αριθμό : "))
di = 0
for i in range(number):
    di=di+number%10
    number=number/10
if di%9==0:
  print "Ο αριθμός διαιρείται με το 9"
else:
  print "Ο αριθμός δεν διαιρείται με το 9"
