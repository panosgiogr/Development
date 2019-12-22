digits = 0
number=int(input("Δώσε έναν αριθμό : "))
num=number
while num>0:
  num=num/10
  digits+=1
print "Ο αριθμός των ψηφίων του αριθμού",number," είναι :",digits
