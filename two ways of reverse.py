a=int(input("enter the number"))
if a>9999 and a<100000:
    b=a//10
    c=a%10
    d=b//10
    e=b%10
    f=d//10
    g=d%10
    h=f//10
    i=f%10
    c=str(c)
    e=str(e)
    g=str(g)
    i=str(i)
    h=str(h)
    print(c+e+g+i+h)
else:
    print("not reverse")    