# 2. Sum of Odd Numbers Problem: Calculate the sum of all odd numbers from 1 up to a given number n.
n = int(input("Enter a number n: "))   # user le dekheko number lai integer ma badalne

total = 0                      # sum rakhne dabba, suru ma 0

for i in range(1, n + 1):      # 1 dekhi n samma
    if i % 2 != 0:             # odd ho ki haina check garne
        total += i             # odd bhaye total ma jodne

print("Sum of odd numbers from 1 to", n, "is:", total)