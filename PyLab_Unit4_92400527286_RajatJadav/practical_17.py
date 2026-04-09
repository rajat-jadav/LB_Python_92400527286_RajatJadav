# Practical 17: Create a dictionary with number as key and its square as value, from 1 to n

n = int(input("Enter the value of n: "))
square_dict = {i: i ** 2 for i in range(1, n + 1)}
print("Dictionary:", square_dict)
