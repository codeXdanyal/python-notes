# String Initialization

"""
str = "This is a String"
str1 = 'Danyal khan'

"""

# Escape Sequence Character

"""
txt = "My name is danyal. \n And i am \tdeveloper"

print(txt)
# Concatenation
a = "hello"
b = "worlds"
print(a + b)
"""
# Length of a string

"""
final_str = str + " " + str1
print(len(final_str))

"""
# Indexing
"""
name = "Danyal khan"
ch = name[4]
print(ch)  # a
"""

# Slicing

"""
name = "danyal khan"
print(name[7 : len(name)])  # end char will not be included
print(name[4:])  # means [4 to len(name)]
print(name[:4])  # means [0:4]
"""

# Negative index

# print(name, name[-5:-1])  # here also end index will not be included

# Some String Methods
"""

str = "i am learning python"

str.endswith("thon")  # return true if strings endswith substr.
str.capitalize()  # capitilize 1st letter
str.replace("python", "javascript")  # replace all occurences of old value with new value
str.find("python")  # return 1st index of first occurence
str.count("a")  # counts the occurence of substr in string
str.split() #split string into list
str.split(",") #split stribg seperated by comma into list

"""
