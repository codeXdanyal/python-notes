# Practice

# Practice 01
# Print the elements of the following list using a loop. [1, 4, 9, 1625, 36, 49, 64, 81, 100]
"""
list = [1, 4, 9, 1625, 36, 49, 64, 81, 100]

for ele in list:
    print(ele)
"""

# Practice 02
# Search for a number x in this tuple using loop: (1, 4, 9, 1625, 36, 49, 64, 81, 100)
"""
nums = (1, 4, 9, 1625, 36, 49, 64, 81, 100, 49)
x = 49
idx = 0
for ele in nums:
    if ele == x:
        print("Found at :", idx)
        break

    idx += 1
"""
