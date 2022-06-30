num1 = float(input("Enter the first number: "))
op = input("Enter the operation. (+,-,*,/) ")
num2 = float(input("Enter the next number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Please give a known operator (+,-,*,/)")