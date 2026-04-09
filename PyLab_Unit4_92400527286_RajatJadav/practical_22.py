# Practical 22: Read text file with numbers and display total and average
# First, create a sample file with numbers

sample_file = "numbers.txt"

# Create sample file
with open(sample_file, 'w') as f:
    f.write("10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n")

print(f"Reading numbers from '{sample_file}':\n")
numbers = []

with open(sample_file, 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            num = float(line)
            numbers.append(num)
            print(num)

total = sum(numbers)
average = total / len(numbers) if numbers else 0

print(f"\nTotal   : {total}")
print(f"Average : {average:.2f}")
