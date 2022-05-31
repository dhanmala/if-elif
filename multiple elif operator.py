a=int(input("enter first number"))
b=int(input("enter second number"))
operator=input("enter operator")
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b) 
elif operator=="/":
    print(a/b) 
elif operator=="//":
    print(a//b)
elif operator=="%":
    print(a%b)
elif operator=="**":
    print(a**b)
else:
    print("none of above")           
