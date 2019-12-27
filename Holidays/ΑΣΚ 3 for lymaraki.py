d=raw_input("Δώσε προορισμό :")
t=raw_input("Δώσε μέσο μεταφοράς :")
days=int(input("Δώσε ημέρες διαμονής :"))
people=int(input("Δώσε αριθμό ατόμων:"))
value_per_customer=0
if d=="Κρήτη" and days==3 and t=="Αεροπλάνο":
    value_per_customer=400
elif d=="Ρόδος" and days==3 and t=="Αεροπλάνο":
    value_per_customer=500
elif d=="Μύκονος" and days==3 and t=="Αεροπλάνο" or d=="Κρήτη" and days==3 and t=="Πλοίο":
    value_per_customer=550
elif d=="Κρήτη" and days==5 and t=="Αεροπλάνο":
    value_per_customer=600
elif d=="Μύκονος" and days==3 and t=="Αεροπλάνο" or d=="Μύκονος" and days==3 and t=="Πλοίο":
    value_per_customer=650
elif d=="Ρόδος" and days==5 and t=="Αεροπλάνο" or (d=="Ρόδος" and days==3 and t=="Πλοίο"):
    value_per_customer=700
elif d=="Κρήτη" and days==5 and t=="Πλοίο":
    value_per_customer=750
elif d=="Μύκονος" and days==5 and t=="Πλοίο":
    value_per_customer=850
elif d=="Ρόδος" and days==5 and t=="Πλοίο":
    value_per_customer=900
print "Σύνολο για",people," επιβάτες με προορισμό :",d," είναι :",value_per_customer*people
