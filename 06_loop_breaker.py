# Task 6: The Loop Breaker
# Loop from 10 to 20:
# - If divisible by 4 -> pass
# - If number is 13 -> continue
# - If number is 18 -> break

for number in range(10, 21):
    if number % 4 == 0:
        pass
    elif number == 13:
        continue
    elif number == 18:
        break

    print(number)
