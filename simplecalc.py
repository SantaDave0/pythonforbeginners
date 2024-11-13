#simple calculator
#will take only two numbers
# x and y



x = int(input("enter your first number: "))

y = int(input("enter your second number: "))

op = input("enter your operator: ")

sum = x + y
diff = x - y
multiplication = x * y
quotient = x / y
#dff -, quotient /, product *
if(op == "+"):
    print(sum)
elif(op == "-"):
    print(diff)
elif(op == "*"):
    print(multiplication)
elif(op=="/"):
    print(quotient)

