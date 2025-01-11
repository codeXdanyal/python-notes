# A built-in data type that lets us create immutable sequence of values.

# Similar to list but its values cannot be changed.

tup = (1, 2, 3, 4, 'five', 1, 2, 1)
print(tup)
print(type(tup))
print(len(tup))

cup = (1,)  #removing comma will make it integer instead of tupple
print(cup)
print(type(cup))


# Tupple Methods
 
print("Number of occurence :", tup.count(1)) #count total occurences
print("First occurence :", tup.index(4))  #return index of first occurence