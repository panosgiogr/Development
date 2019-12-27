destination=raw_input("Δώσε προορισμό : ")
transportation=raw_input("Δώσε μέσο μεταφοράς : ")
days=int(input("Δώσε ημέρες διαμονής : "))
people=int(input("Δώσε αριθμό ατόμων"))
value_per_customer=400
if transportation=="Πλοίο":
    if destination=="Κρήτη":
        value_per_customer+=150
    elif destination=="Ρόδος":
        value_per_customer+=300
    elif destination=="Μύκονος":
        value_per_customer += 250
    if days==5:
        value_per_customer+=200
elif transportation=="Αεροπλάνο":
    if destination=="Ρόδος":
        value_per_customer+=100
    elif destination=="Μύκονος":
        value_per_customer += 150
    if days==5 and destination=="Κρήτη" or destination=="Ρόδος":
        value_per_customer+=200
    else:
        value_per_customer+=100
print "Σύνολο για",people," επιβάτες με προορισμό :",destination," :",value_per_customer*people
