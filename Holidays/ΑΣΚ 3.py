destination=raw_input("���� ��������� : ")
transportation=raw_input("���� ���� ��������� : ")
days=int(input("���� ������ �������� : "))
people=int(input("���� ������ ������"))
value_per_customer=400
if transportation=="�����":
    if destination=="�����":
        value_per_customer+=150
    elif destination=="�����":
        value_per_customer+=300
    elif destination=="�������":
        value_per_customer += 250
    if days==5:
        value_per_customer+=200
elif transportation=="���������":
    if destination=="�����":
        value_per_customer+=100
    elif destination=="�������":
        value_per_customer += 150
    if days==5 and destination=="�����" or destination=="�����":
        value_per_customer+=200
    else:
        value_per_customer+=100
print "������ ���",people," �������� �� ��������� :",destination," :",value_per_customer*people
