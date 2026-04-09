# Practical 11: Input a number and display its Factorial

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0:
    print("Factorial of 0 = 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} = {factorial}")
