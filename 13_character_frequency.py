# Task 13: Character Frequency Counter
# Count how many times each character appears in a string.

text = input("Enter a string: ")

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print("Character frequencies:")
print(frequency)
