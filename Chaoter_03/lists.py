# Lists

"""
list = [1, 'abc', 8347.3]
print(list)
"""

# Lists are mutable
"""
Student[2] = 44
print(Student)  # 33 becomes 44
"""

# print(Student[9])  #IndexError: list index out of range

# List Slicing
# syntax: list_name[start:stop] Ending index is not included

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])
print(numbers[:5])
print(numbers[3:])
print(numbers[-9:-1])
"""

# List Methods

"""
alpha = ["one", "two", "three", "two", "three"]
print(alpha)

alpha.append("four")
print(alpha)

alpha.sort()
print(alpha)

alpha.sort(reverse=True)
print(alpha)

alpha.reverse()
print(alpha)

alpha.insert(5, "six")
print(alpha)

alpha.remove("three")  # remove first occurence of element
print(alpha)

alpha.pop(3)  # remove first occurence of element
print(alpha)  # remove element from particular index

alpha.append("one")
x = alpha.count("one")
print("count", x)

name = "Danyal khan"
arr = list(name)
print(arr)

list = name.split()
print(list)
# list = name.split(",")
# list = name.split(",", 2)

"""
