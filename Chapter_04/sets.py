# Sets in python
"""
Sets is the collection of the unordered (no index) items.
Each element is the set must be unique & immutable
We can't store list & dictionary in our sets because they are immutable.
Only values can be stored not keys.
Duplicates values only count single time
Sets are mutable means we can add remove elements but the elements of set is immutable we can't change them
Set ---> Mutable  | Set Elements ---> Immutable
"""
num = {1, 2, 3, 4, 5, 6}
num2 = {
    1,
    2,
    3,
    4,
    4,
}  # repeated elements stored only once, so it resolved to {1, 2, 3, 4}

print(num)
print(type(num))
print(num2)


# Empty Set Syntax
null_set = {}  # it's not a Set it's a dictionary
print("null_set", type(null_set))

# Correct Syntax for Empty Set
empty_set = set()
print("Empty_set", type(empty_set))

# Set with other data types
collection = {1, 2, "one", "two", 3.5, True, ("one", "two", "three")}
print(collection)
print(len(collection))

# Set Methods
empty_set = set()

empty_set.add(1)  # adds an element
empty_set.add(2)  # adds an element
empty_set.add(3)  # adds an element
empty_set.add(4)  # adds an element
empty_set.add((1, 2, 3, 4, 5, 6))  # adds an element
empty_set.remove(1)  # removes the element
print(empty_set.pop())  # removes a random value
empty_set.clear()  # empties the set
print(empty_set)

# imp Methods

set_one = {1, 2, 3}
set_two = {2, 3, 4, 5, 6}

print(set_one)
print(set_two)

set_3 = set_one.union(set_two)  # merge the elements
print(set_3)

set_4 = set_one.intersection(set_two)  # return common values
print(set_4)


# Hashing

# it's a algorithm that converts original value into another value
# Mutable ---> hashable value Means whos values change over time
# Immutable ---> non-hashable value Means whos values don't change over time
