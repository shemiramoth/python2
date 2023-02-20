age = eval(input("How old are you?"))
if age<18:
    print("You can't sign up")
else:
    print("Continue to create account")
    if age>22:
        print("You are too old for this")
    else :
        print("You are elligible")
        