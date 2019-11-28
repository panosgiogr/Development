payments=0
employees=0
max_payment=0
max_payment_employee_name=""
employee_name=raw_input("Δώσε όνομα υπαλλήλου : ")
while employee_name!="Τέλος":
    employees+=1
    employee_payment=input("Δώσε μισθό του υπαλλήλου με όνομα "+employee_name+" : ")
    payments+=employee_payment
    if employee_payment>max_payment:
        max_payment=employee_payment
        max_payment_employee_name=employee_name
    employee_name = raw_input("Δώσε όνομα υπαλλήλου : ")
print "Τον μεγαλύτερο μισθό τον παίρνει ο/η :",max_payment_employee_name
print "Ο Μ.Ο. όλων των μισθών είναι :",float(payments/employees)