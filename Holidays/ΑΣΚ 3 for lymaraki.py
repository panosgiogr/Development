d=raw_input("���� ��������� :")
t=raw_input("���� ���� ��������� :")
days=int(input("���� ������ �������� :"))
people=int(input("���� ������ ������:"))
value_per_customer=0
if d=="�����" and days==3 and t=="���������":
    value_per_customer=400
elif d=="�����" and days==3 and t=="���������":
    value_per_customer=500
elif d=="�������" and days==3 and t=="���������" or d=="�����" and days==3 and t=="�����":
    value_per_customer=550
elif d=="�����" and days==5 and t=="���������":
    value_per_customer=600
elif d=="�������" and days==3 and t=="���������" or d=="�������" and days==3 and t=="�����":
    value_per_customer=650
elif d=="�����" and days==5 and t=="���������" or (d=="�����" and days==3 and t=="�����"):
    value_per_customer=700
elif d=="�����" and days==5 and t=="�����":
    value_per_customer=750
elif d=="�������" and days==5 and t=="�����":
    value_per_customer=850
elif d=="�����" and days==5 and t=="�����":
    value_per_customer=900
print "������ ���",people," �������� �� ��������� :",d," ����� :",value_per_customer*people
