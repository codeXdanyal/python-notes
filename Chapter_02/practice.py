#  Practice 01


# Write a program to input user's first name & print its length without counting spacing

"""

name = input("Enter your name :")
space_removed = name.replace(" ", "")
print(len(space_removed))

"""

#  Practice 02

# Write a program to find the occurence of '$' in a string"

"""
str = "hello $ my name is $ and i am $"
print(str.count("$"))

"""
# Practice 03

# Write a program that takes a user's full name (first and last name) as input and returns username in lowercase letters:

"""

full_name = input("Enter your Full Name : ")

space_freeName = full_name.replace(" ", "")

username =  "@" + space_freeName + str(len(space_freeName)) 

print(username)

"""