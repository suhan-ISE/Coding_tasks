# Task 5: Prime Number Finder
# Find and print the first 10 prime numbers using a while loop.

count = 0
number = 2

while count < 10:
    is_prime = True
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(number, end=" ")
        count += 1

    number += 1

print()
