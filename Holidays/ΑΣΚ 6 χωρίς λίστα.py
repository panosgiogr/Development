number=int(input("���� ���� ������ : "))
while number>=100 or number<10:
    number = int(input("���� ���� ������ : "))
digit0=number/10
digit1=number%10


print "�� ����� ��� �� ����� ����������� � �������",number," ����� ��",digit0," ��� ��",digit1
print "�� �������� ��� ������",digit0,"+",digit1," ����� :",digit0+digit1
print "� �������������� ������� ���",number," ����� ��",str(digit1)+str(digit0)
