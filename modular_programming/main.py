import operators
import others
import trig

# x = operators.add(12,34)
# print(x)

# y = operators.subtract(34,12)
# print(y)

# q = operators.multiply(5,2)
# print(q)

# w = operators.divide(4,2)
# print(w)

# a = others.cube(9)
# print(a)

operator = input("Enter operator: ")

#get numbers
if operator == "cube":
    number = eval(input("Enter number: "))
    p = others.cube(number)
    print(p)

elif operator == "tan":
    angle = eval(input("Enter angle in degrees: "))
    tan_of_angle = trig.get_tan(angle)
    print(tan_of_angle)

elif operator == "cos":
    angle = eval(input("Enter angle in degrees: "))
    cos_of_angle = trig.get_cos(angle)
    print(cos_of_angle)

elif operator == "sin":
    angle = eval(input("Enter angle in degrees: "))
    sin_of_angle = trig.get_sine(angle)
    print(sin_of_angle)
    

else:
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))

    if operator == "+":
        x = operators.add(num1,num2)
        print(x)

    elif operator == "-":
        y = operators.subtract(num1,num2)
        print(y)

    elif operator == "*" or operator == "x" or operator == "X":
        z = operators.multiply(num1,num2)
        print(z)

    elif operator == "/":
        w = operators.divide(num1,num2)
        print(w)


