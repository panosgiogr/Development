number=int(input("Δώσε έναν αριθμό : "))
while number>=100 or number<10:
    number = int(input("Δώσε έναν αριθμό : "))
digit0=number/10
digit1=number%10


print "Τα ψηφία απο τα οποία αποτελείται ο αριθμός",number," είναι το",digit0," και το",digit1
print "Το άθροισμα των ψηφίων",digit0,"+",digit1," είναι :",digit0+digit1
print "Ο αντεστραμμένος αριθμός του",number," είναι το",str(digit1)+str(digit0)
