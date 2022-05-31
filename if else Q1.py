#minimum number among 3 numbers
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a<b and a<c:
    print("a is minimum")
elif b<a and b<c:
    print("b is minimum")
elif c<a and c<b:
    print("c is minimum") 
else:
    print("none") 
         