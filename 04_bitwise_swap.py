# Task 4: Bitwise Swap (Advanced)
# Swap two integers without a third variable and without multiple assignment.
# XOR swap works because a ^ a = 0 and a ^ 0 = a.

a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)
