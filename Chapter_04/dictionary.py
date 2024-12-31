# Dictionary

# Dictionary are used to store data values in key/value pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys
# we can store any type of data in dictionary.
# we cannot make the keys names of dictionary to list and dictionary but we can make it strings, numbers, float, tuple or booleun value.
# we can't use dict & list as dictionary key names bcz both are mutable they can change.


student = {
    "name": "danyal",
    "age": 19,
    "marks": 99.88,
    "tup": ("hello", "world", "danyal"),
    "list": [1, 2, 34, 44, 4],
    "single": True,
    13: 54,
}

print(student)
print(type(student))

# Accessing dictionary keys/values

print(student["name"])
print(student["tup"][1])
print(student["list"][3])

# Adding new values

student["Nickname"] = "Developer"
print(student)

# Assigning new values

student["name"] = "Danyal khan"  # Overwrite
print(student)

# Creating a null/empty dictionary

null_dict = {}
null_dict["name"] = "Danyal khan"
print(null_dict)

# Nested Dictionary

courses = {"marks": {"Math": 90, "phy": 78.2, "chemistry": "fail"}, "result": "fail"}
print(courses)
print(courses["marks"])
print(courses["marks"]["phy"])

# Dictionary Methods

noraml_dict = {"name": "danyal", "age": 19, "marks": 90.2, "Address": "London"}

print(noraml_dict.keys())  # return keys of dictionary.
print(type(noraml_dict.keys()))  # return type of dictionary keys which is dict_keys.
print(list(noraml_dict.keys()))  # Converting dict_keys to list.
print(len(noraml_dict.keys()))  # return length of dictionary.

print(noraml_dict.values())  # return type of dictionary values which is dict_values.
print(list(noraml_dict.values()))  # Converting values to list.

print(noraml_dict.items())  # reuturn all key/values pairs as tuples.
pair = list(noraml_dict.items())
print(pair[0])  # return key / value as tuple.

print(noraml_dict.get("name"))  # returns the key according to value
# normal_dict.get() & normal_dict["key"] both ways are same but ' .get() ' method return None when there is no matching key & the square bracket Notation  will return error.

# Simple Example why not to use square bracket noation

"""
print("BEFORE")  # Execute
print(noraml_dict["nmae2"])  # error
print("After")  # Will Not execute and this is the problem

"""
# Update Method

my_dict = {"name": "danyal", "age": 19}
new_dict = {"Address": "London", "name": "Danyal khan"}
my_dict.update(new_dict)
print(my_dict)
