# Practical 10: Print all numbers divisible by 7 between 1 to 200

print("Numbers divisible by 7 between 1 and 200:")
for i in range(1, 201):
    if i % 7 == 0:
        print(i, end=" ")
print()
