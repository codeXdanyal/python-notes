# Practice

# Practice 01
# Print Numbers from 1 to 100.
"""
i = 1
while i <= 100:
    print(i)
    i += 1  
"""

# Practice 02
# Print Numbers from 100 to 1.
"""
j = 100
while j >= 1:
    print(j)
    j -= 1 
"""

# Practice 03
# Print Multiplication table of n.
"""
number = int(input("Table name : "))
count = 1
while count <= 10:
    table = number * count
    print(number, "x", count, "=", table)
    count += 1   
"""

# Practice 04
# Print the elements of the following list using a loop. [1, 4, 9, 1625, 36, 49, 64, 81, 100]
"""
num_list = [1, 4, 9, 1625, 36, 49, 64, 81, 100]

i = 04
while i < len(num_list):
    print(num_list[i])
    i += 1   
"""

# Practice 05
# Search for a number x in this tuple using loop: [1, 4, 9, 1625, 36, 49, 64, 81, 100]

"""
num_tuples = (1, 4, 9, 1625, 36, 49, 64, 81, 100)
x = int(input("Enter X Number : "))
i = 0
while i < len(num_tuples):
    if num_tuples[i] == x:
        print("Found at Index ", i)
        break
    else:
        print("Finding...")
    i = i + 1    
"""

# Practice 06
# Print all characters of string using loop
"""
str = input("Enter Your Name : ")
idx = 0
while idx < len(str):
    print(str[idx])
    idx += 1
"""

# Practice 06
#  Printing ODD Numbers
"""
x = 0
while x <= 100:
    if x % 2 == 0:

        x += 1
        continue
    print(x)
    x += 1
"""

# Practice 08
# WAP to find the sum of first natural numbers.
n = 7
sum = 0
i = 1
while i <= n:
    sum += n
    i += 1

print("sum =", sum)
