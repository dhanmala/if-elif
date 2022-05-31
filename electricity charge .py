unit=int(input("enter the unit charge"))
if unit<50:
    amount=unit*0.50
    sur=50
    print(amount)
elif unit<=100:
    amount=unit*0.75
    sur=75
    print(amount)    
elif unit>=100:
    amount=unit*1.20
    sur=20
    print(amount) 
else:
    amount=2.50+1.50(unit-500)*1.50
    sur=20
    total=amount-sur
    print("electricity bill=1.50",total)
    