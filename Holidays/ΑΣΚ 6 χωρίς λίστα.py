number=int(input("Δώσε έναν αριθμό : "))
while number>=100 or number<10:
    number = int(input("Δώσε έναν αριθμό : "))
digit1=str(number%10)
digit0=str((number-int(digit1))/10)

print "Τα ψηφία απο τα οποία αποτελείται ο αριθμός",number," είναι το",digit0," και το",digit1
print "Το άθροισμα των ψηφίων",digit0,"+",digit1," είναι :",int(digit0)+int(digit1)
print "Ο αντεστραμμένος αριθμός του",number," είναι το",digit1+digit0
