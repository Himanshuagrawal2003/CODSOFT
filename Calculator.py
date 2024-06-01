Number1=int(input("Enter The First Value: "))
Number2=int(input("Enter The Second Value: "))
operator=input("Choose Operator[+,-,*,/]:")
if operator=="+":
    print(Number1+Number2)
elif operator=="-":
    print(Number1-Number2)
elif operator=="*":
    print(Number1*Number2)
elif operator=="/":
    print(Number1/Number2)
else:
    print("Wrong operation Try Again")