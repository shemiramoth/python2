#ask for input, check if -ve
#if -ve tell user wrong entry
#if +ve check whether greater than 50
#if greater than 50 divide by to
#if less than 50 tell user no is less tham 50 and is correct
no = eval(input("pick a number between 0 and 50"))
if no<0:
    print("number is less than 0, please try again") 
else:
    print("number is correct") 
    if no>50:
            x = no/2
    elif no<50:
        print("number is correct")
