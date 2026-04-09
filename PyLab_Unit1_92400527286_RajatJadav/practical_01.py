# Practical 1: INPUT two variables and print Addition, Subtraction, Multiplication and Division

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"Addition       : {a + b}")
print(f"Subtraction    : {a - b}")
print(f"Multiplication : {a * b}")
if b != 0:
    print(f"Division       : {a / b}")
else:
    print("Division       : Cannot divide by zero")
