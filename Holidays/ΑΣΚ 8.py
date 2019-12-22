number=int(input("Δώσε έναν αριθμό : "))
num=number
c=0
while num>0:
  num=num/10
  c+=1
new_num=0
for i in range(c):
    new_num=(num/(10**c-1))
    num-=new_num*(10**c-1)
    c-=1
    print new_num
    
