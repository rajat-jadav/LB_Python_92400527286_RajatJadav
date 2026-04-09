# Practical 18: Accept comma-separated numbers and generate a list and a tuple

data = input("Enter comma-separated numbers: ")
num_list = [int(x.strip()) for x in data.split(",")]
num_tuple = tuple(num_list)

print("List :", num_list)
print("Tuple:", num_tuple)
