number=int(input("���� ���� ������ : "))
num_str=str(number)
while len(num_str)!=2:
    number = int(input("���� ���� ������ : "))
    num_str=str(number)
print "�� ����� ��� �� ����� ����������� � �������",num_str," ����� ��",num_str[0]," ��� ��",num_str[1]
print "�� �������� ��� ������",num_str[0],"+",num_str[1]," ����� :",int(num_str[0])+int(num_str[1])
print "� �������������� ������� ���",num_str," ����� ��",num_str[1]+num_str[0]
