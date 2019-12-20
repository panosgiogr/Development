number=int(input("Δώσε έναν αριθμό : "))
num_str=str(number)
while len(num_str)!=2:
    number = int(input("Δώσε έναν αριθμό : "))
print num_str[0],num_str[1]
print int(num_str[0])+int(num_str[1])
print num_str[1]+num_str[0]
