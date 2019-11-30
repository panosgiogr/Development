employees=["Panos Gio","Mary Jio","John Tio"]# ...
payments=[1500,1550,1500] # ...
employees=[]
payments=[]
max_payment=payments[0]
max_payment_name=[]

for i in range(1,31,1):
    employee=raw_input("Δώσε ονοματεπώνυμο : ")
    employees.append(employee)
    payment=int(input("Δώσε μισθό του/της "+employee+" : "))
    while payment<0:
        payment = int(input("Δώσε μισθό του/της " + employee + " μη αρνήτικό : "))
    payments.append(payment)
    if payment>max_payment:
        max_payment=payment
for i in range(0,30,1):
    if payment[i]==max_payment:
        max_payment_name.append(employees[i])
print "Ο μεγαλύτερος μισθός είναι :",max_payment
print "Οι υπάλληλοι με τον ίδιο μισθό είναι οι :",max_payment_name
