product_name=[]
product_stock=[]
product_price=[]
products_count=len(product_name)
stock_house_value=[]
for i in range (products_count):
    summ=product_stock[i]*product_price[i]
    stock_house_value.append(summ)
stock_house_value_var=0
for i in range(products_count):
    stock_house_value_var=+stock_house_value[i]
print "Το συνολικό ποσό που η αποθήκη έχει δαπανήσει είναι :",stock_house_value_var
product_low_stock=[]
for i in range(products_count):
    if product_stock[i]<5:
        product_low_stock.append(product_name[i])
print "Προϊόντα διαθεσιμότητα < 5:",product_low_stock
products_high_price_list=[]
products_high_price=0
for i in range(products_count):
    if product_price[i]>=products_high_price:
        products_high_price=product_price[i]
        products_high_price_list.append(product_name[i])
print "Το ποιο/ποια ακριβό/ακριβά προιόν/προιόντα είναι :",products_high_price_list
product_low_stock=product_stock[i]
product_low_stock_name=product_name[i]
for i in range(products_count):
    if product_stock[i]<product_low_stock and product_stock!=0:
        product_low_stock=product_name[i]
        product_low_stock_name=product_name[i]
print "Το προιόν με τη μικρότερη ποσότητα άλλα μη μηδενική είναι το :",product_low_stock_name