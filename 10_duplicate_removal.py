# Task 10: Duplicate Removal
# Single-line solution using a set.
# Note: set removes duplicates but does not guarantee original order.

numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))

unique_values = list(set(numbers))

print("Unique values:", unique_values)
