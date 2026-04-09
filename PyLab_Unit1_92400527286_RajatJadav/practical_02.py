# Practical 2: Input 2 numbers and an arithmetic operator, display the result

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(f"Result: {a + b}")
elif op == '-':
    print(f"Result: {a - b}")
elif op == '*':
    print(f"Result: {a * b}")
elif op == '/':
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator!")
