# Practical 4: Input Principal Amount, Rate and Year and display Compound Interest

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest (%): "))
t = float(input("Enter Time (Years): "))

ci = p * ((1 + r / 100) ** t) - p
print(f"Compound Interest = {ci:.2f}")
