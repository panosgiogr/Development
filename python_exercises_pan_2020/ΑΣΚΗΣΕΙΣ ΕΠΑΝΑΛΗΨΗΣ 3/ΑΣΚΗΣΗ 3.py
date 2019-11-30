born_count=[12,3,5,4,1,6,12]
born_days =["Κυριακή","Δευτέρα","Τρίτη","Τετάρτη","Πέμπτη","Παρασκευή","Σάββατο"]
born_max=born_count[0]
for i in range(0,7,1):
    if born_max<born_count[i]:
        born_max=born_count[i]
print "H ημέρα με τον μεγαλύτερο αριθμό γεννήσεων στο μαιευτήριο είναι η ",born_days[born_count[born_max]]