# Practical 7: Input age of person and display appropriate message

age = int(input("Enter your age: "))

if age < 12:
    print("You are Kid")
elif 12 <= age <= 17:
    print("You are Teenager")
elif 18 <= age <= 60:
    print("You are Adult")
else:
    print("You are Senior Citizen")
