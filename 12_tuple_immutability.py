# Task 12: Tuple Immutability Test
# Tuples cannot be changed after creation.
# Attempting to change an element raises TypeError.

my_tuple = (10, 20, 30)

try:
    my_tuple[1] = 99
except TypeError as error:
    print("Error:", error)
    print("Tuples are immutable, so their elements cannot be changed.")

print("Original tuple:", my_tuple)
