#simple calculator
#will take only two numbers
# x and y

import methods

x = int(input("enter your first number: "))

y = int(input("enter your second number: "))

op = input("enter your operator: ")




diff = x - y
multiplication = x * y
quotient = x / y
#dff -, quotient /, product *
if(op == "+"):
    print(methods.sum(x,y))
elif(op == "-"):
    print(diff)
elif(op == "*"):
    print(multiplication)
elif(op=="/"):
    print(quotient)

