# Practical 25: Demo for import module in Python

# Importing standard library modules
import math
import random
import datetime
import os

print("=== Import Module Demo ===\n")

# math module
print("--- math module ---")
print(f"math.pi         = {math.pi:.4f}")
print(f"math.sqrt(144)  = {math.sqrt(144)}")
print(f"math.factorial(5) = {math.factorial(5)}")
print(f"math.ceil(4.2)  = {math.ceil(4.2)}")
print(f"math.floor(4.9) = {math.floor(4.9)}")

# random module
print("\n--- random module ---")
print(f"random.random()         = {random.random():.4f}")
print(f"random.randint(1, 100)  = {random.randint(1, 100)}")
print(f"random.choice([a,b,c])  = {random.choice(['apple', 'banana', 'cherry'])}")

# datetime module
print("\n--- datetime module ---")
now = datetime.datetime.now()
print(f"Current Date & Time = {now.strftime('%Y-%m-%d %H:%M:%S')}")

# os module
print("\n--- os module ---")
print(f"Current Directory = {os.getcwd()}")
