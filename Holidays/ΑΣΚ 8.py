number=int(input("���� ���� ������ : "))
di = 0
for i in range(number):
    di=di+number%10
    number=number/10
if di%9==0:
  print "� ������� ���������� �� �� 9"
else:
  print "� ������� ��� ���������� �� �� 9"
