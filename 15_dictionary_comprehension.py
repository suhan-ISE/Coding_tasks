# Task 15: Dictionary Comprehension
# From {'a': 1, 'b': 2, 'c': 3, 'd': 4},
# create a dictionary containing only values greater than 2.

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

filtered_data = {key: value for key, value in data.items() if value > 2}

print("Filtered dictionary:", filtered_data)
