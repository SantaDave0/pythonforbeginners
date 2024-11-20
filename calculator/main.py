import functions
print("Hello this is a calculator app")

#first input

x = int(input("enter your first number: "))
y = int(input("enter your second number: "))


#operator

operator = input("enter your first operator: ")

if(operator == "+"):
    print(functions.sum(x,y))

elif(operator == "-"):
    print(functions.difference(x,y))

elif(operator == "/"):
    print(functions.quotient(x,y))

elif(operator == "*"):
    print(functions.multiply(x,y))

else:
    print("your are not ana operator: ")