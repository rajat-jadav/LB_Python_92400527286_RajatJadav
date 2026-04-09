# Practical 8: Input marks of 4 subjects and display Total, Percentage, Result and Grade

s1 = float(input("Enter marks of Subject 1: "))
s2 = float(input("Enter marks of Subject 2: "))
s3 = float(input("Enter marks of Subject 3: "))
s4 = float(input("Enter marks of Subject 4: "))

total = s1 + s2 + s3 + s4
percentage = total / 4

if s1 < 40 or s2 < 40 or s3 < 40 or s4 < 40:
    result = "FAIL"
    grade = "With Held**"
else:
    result = "PASS"
    if percentage >= 70:
        grade = "Distinction"
    elif percentage >= 60:
        grade = "First Class"
    elif percentage >= 50:
        grade = "Second Class"
    else:
        grade = "Pass Class"

print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Result     : {result}")
print(f"Grade      : {grade}")
