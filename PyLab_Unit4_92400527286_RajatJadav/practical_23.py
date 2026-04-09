# Practical 23: Compute frequency of words from input, sorted alphanumerically

import re

text = input("Enter a sentence: ")
words = re.findall(r'\b\w+\b', text.lower())

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("\nWord Frequencies (sorted alphanumerically):")
for word in sorted(freq.keys()):
    print(f"{word} : {freq[word]}")
