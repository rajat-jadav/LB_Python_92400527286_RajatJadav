# Practical 15: Print factorial number using function

def factorial(n):
    if n < 0:
        return "Undefined"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} = {factorial(num)}")
