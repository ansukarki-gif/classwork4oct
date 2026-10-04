# 3. Multiplication Table Printer Problem: Print the multiplication table for a given number up to 10, but skip the third iteration.
n = int(input("Enter a number: "))

for i in range(1, 11):
    if i == 3:
        continue
    print(n, "x", i, "=", n * i)