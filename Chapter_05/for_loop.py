# Loops in Python

# For Loops are used for sequential traversal. For traversing list, string, tuples etc. ---> Similar to For-of & For-in loop in Javascript

# For Loops
# Syntax:
"""
for el in list:
    #Some Work
"""

# Example on List
"""
list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 00]

for i in list:
    print(i)  # Print each Element of list
"""

# Example on tuple
"""
tup = (11, 22, 33, 44)
for i in tup:
    print(i)
"""

# For loop with else
# Syntax:
"""
for el in list:
    Some work
else:
    Work when loops ends
"""

# Example

str = "Danyal"
for char in str:
    print(char)
else:
    print("Loop Ends")  # Execute when loops ends
