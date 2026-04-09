# Practical 20: Read names from keyboard and store into a text file

filename = "names.txt"
print("Enter names (type 'done' to stop):")

with open(filename, 'w') as f:
    while True:
        name = input("Enter name: ")
        if name.lower() == 'done':
            break
        f.write(name + "\n")

print(f"Names saved to '{filename}' successfully.")
