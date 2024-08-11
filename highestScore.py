num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
operation = input("Pick operation from this list (+,-,*,/) ")

if operation == "+":
    ans = num1 + num2
    print(f"{num1} + {num2} = {ans}")
elif operation == "-":
    ans = num1 - num2
    print(f"{num1} - {num2} = {ans}")
elif operation == "*":
    ans = num1 * num2
    print(f"{num1} * {num2} = {ans}")
else:
    ans = num1 / num2
    print(f"{num1} / {num2} = {ans}")
