'''
ATM Machine 
'''

name='bhanu'
password='1234'
user_name=input("enter the User Name:")
passwords=input("enter the Password:")
d='''
    1=Debit
    2=Credit
    3=Mini Statement
    4=Exit
'''
Amount=2000
if name==user_name and password==passwords:
    print(d)
    option=int(input("enter the option:"))
    if option==1:
        Debit_amount=int(input("enter the amount:"))
        print("amount after Debit",Amount-Debit_amount)
    elif option==3:
        Mini_statement=int(input("enter the amount:"))
        print("Amount",Amount)

    

else:
    print('In correct')


