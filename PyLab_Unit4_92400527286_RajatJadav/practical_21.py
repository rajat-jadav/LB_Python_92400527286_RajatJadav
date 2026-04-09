# Practical 21: Read any text file line by line

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as f:
        print(f"\nContents of '{filename}':")
        for line_no, line in enumerate(f, start=1):
            print(f"Line {line_no}: {line}", end="")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
