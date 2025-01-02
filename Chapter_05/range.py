# Range()

# Range function return a sequence of numbers, starting from 0 (by default), and increments by
# 1 (by default), and stops before a specified number.
# Syntax: range(start?, stop, step?)  step ----> increase

"""
for el in range(5):  #range(stop)
    print(el)
    
for el in range(1, 5): #range(start, stop)
    print(el)
    
for el in range(1, 5, 2): #range(start, stop, step)
    print(el)
"""

# Example:
# seq = range(10)

for i in range(5):
    print("range(5) =", i)

print("\n")

for i in range(5, 10):
    print("range(start, stop) =", i)

print("\n")

for i in range(5, 10, 2):
    print("start, stop, step =", i)
