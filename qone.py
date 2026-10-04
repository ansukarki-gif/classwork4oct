# 1. Counting Negative Numbers Problem: 
# Given a list of numbers, count how many are negative. numbers = [2, -3, 4, -5, -6, 7, 8, -9]
numbers = [2, -3, 4, -5, -6, 7, 8, -9]
count = 0                      # start the counter at 0

for num in numbers:            # go through each number
    if num < 0:                # negative means less than 0
        count += 1             # add 1 to the counter

print("Negative numbers:", count)   # Output: 4
