Name=[]
Arxiki=[]

for i in range(1,101,1):
    cd_name=raw_input("Δώσε όνομα "+str(i)+"ου CD : ")
    cd_price=float(input("Δώσε τιμή του "+cd_name+" : "))
    Name.append(cd_name)
    Arxiki.append(cd_price)
customer_cd=raw_input("Δώσε όνομα CD προς αγορά : ")
customer_cd_price=0
if customer_cd in Name:
    arxiki_timi=Arxiki[Name.index(customer_cd)]
    customer_cd_price=arxiki_timi-arxiki_timi*0.30
    print "Ο πελάτης θα πληρώσει :",customer_cd_price," ευρώ"
else:
    print "CD δεν είναι σε προσφορά"