# Practical 3: Input Principal Amount, Rate and Year and display Simple Interest

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest (%): "))
t = float(input("Enter Time (Years): "))

si = (p * r * t) / 100
print(f"Simple Interest = {si}")
