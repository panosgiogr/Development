digits = 0
number=int(input("���� ���� ������ : "))
num=number
while num>0:
  num=num/10
  digits+=1
print "� ������� ��� ������ ��� �������",number," ����� :",digits
