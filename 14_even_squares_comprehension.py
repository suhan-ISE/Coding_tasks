# Task 14: List Comprehension
# Create a list of squares of all even numbers between 1 and 20.

squares = [number ** 2 for number in range(1, 21) if number % 2 == 0]

print("Squares of even numbers:", squares)
