number=int(input("���� ���� ������ : "))
di = 0
for i in range(number):
    di=di+number%10
    number=number/10
    print di
    print number
if di==9:
  print "� ������� ���������� �� �� 9"
else:
  print "� ������� ��� ���������� �� �� 9"

