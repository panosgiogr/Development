number=int(input("���� ���� ������ : "))
while number>=100 or number<10:
    number = int(input("���� ���� ������ : "))
digit1=str(number%10)
digit0=str((number-int(digit1))/10)

print "�� ����� ��� �� ����� ����������� � �������",number," ����� ��",digit0," ��� ��",digit1
print "�� �������� ��� ������",digit0,"+",digit1," ����� :",int(digit0)+int(digit1)
print "� �������������� ������� ���",number," ����� ��",digit1+digit0
