# Task 8: Reverse an Integer
# Use a while loop and // and % operators.

number = int(input("Enter an integer: "))

sign = -1 if number < 0 else 1
number = abs(number)

reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

reversed_number *= sign

print("Reversed integer:", reversed_number)
