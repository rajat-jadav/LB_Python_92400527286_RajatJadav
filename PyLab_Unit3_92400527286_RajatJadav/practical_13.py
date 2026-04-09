# Practical 13: Find numbers divisible by 7 but not multiple of 5, between 2000 and 3200

print("Numbers divisible by 7 but not multiple of 5 (between 2000 and 3200):")
result = [i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
print(result)
