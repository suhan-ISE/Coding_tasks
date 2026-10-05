# Task 7: Nested Conditionals
# Classify a numerical grade:
# A: 90+
# B: 80-89
# C: 70-79
# Fail: below 70

grade = float(input("Enter your grade (0-100): "))

if 0 <= grade <= 100:
    if grade >= 90:
        result = "A"
    else:
        if grade >= 80:
            result = "B"
        else:
            if grade >= 70:
                result = "C"
            else:
                result = "Fail"

    print("Grade:", result)
else:
    print("Invalid grade. Enter a value between 0 and 100.")
