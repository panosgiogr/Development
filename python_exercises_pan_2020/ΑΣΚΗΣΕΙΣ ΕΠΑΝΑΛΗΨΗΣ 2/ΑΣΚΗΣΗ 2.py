#author panosgio
temp=int(input("Δώσε θερμοκρασία ημέρας : "))
avg_temp=0
counter=1
while temp!=-100:
    avg_temp += temp
    counter+=1
    temp = int(input("Δώσε θερμοκρασία ημέρας : "))

print "Η μέση Θερμοκρασία της ημέρασ είναι :",avg_temp/counter,"°C"