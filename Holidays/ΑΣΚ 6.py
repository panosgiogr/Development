number=int(input("Δώσε έναν αριθμό : "))
num_str=str(number)
while len(num_str)!=2:
    number = int(input("Δώσε έναν αριθμό : "))
    num_str=str(number)
print "Τα ψηφία απο τα οποία αποτελείται ο αριθμός",num_str," είναι το",num_str[0]," και το",num_str[1]
print "Το άθροισμα των ψηφίων",num_str[0],"+",num_str[1]," είναι :",int(num_str[0])+int(num_str[1])
print "Ο αντεστραμμένος αριθμός του",num_str," είναι το",num_str[1]+num_str[0]
