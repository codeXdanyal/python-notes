# Practice
# using for & range()

# Practice 01
# Print numbers from 1 to 100
"""
for i in range(1, 101):
    print(i)
"""

# Practice 02
# Print numbers from 100 to 1
"""
for i in range(100, 0, -1):
    print(i)
"""

# Practice 03
# Print the multiplication table of a number n.

n = int(input("Enter number: "))
for i in range(1, 11, 1):
    table = n * i
    print(n, "x", i, "=", table)
