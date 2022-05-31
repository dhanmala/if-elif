guess=int(input("enter the guess number"))
actual_number=int(input("enter actual number"))
if guess<actual_number:
    print("your guess number is too low")
elif guess>actual_number:
    print("your guess was too high") 
else:
    print("not low not high")       
