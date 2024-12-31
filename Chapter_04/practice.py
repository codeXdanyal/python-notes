# Practice_01

# Store following words in a python dictionary

"""

word_meaning = {
    "table": ("a piece of furniture", "list of facts & figures"),
    "cat": "a small animal",
}

print(word_meaning)

"""

# Practice_02

# You are given a list of subjects for students. Assu,e one classroom is requires for 1 subject. How many classromms are needed by all students.

# python, java, c++, python, python, javascript, java, python, java, C++, C

"""
    
subjects = {
    "python",
    "java",
    "C++",
    "python",
    "python",
    "javascript",
    "java",
    "python",
    "java",
    "C++",
    "C",
}

print("Subjects :", subjects)
print("Total Number of classRooms :", len(subjects))

"""

# Practice_03

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty & add one by one. Use Subject name as key & marks as value

"""

student = {}

subject1 = input("First Subject : ")
subject1_marks = int(input("Enter marks : "))
student[subject1] = subject1_marks

subject2 = input("Second Subject : ")
subject2_marks = int(input("Enter marks : "))
student[subject2] = subject2_marks

subject3 = input("Third Subject : ")
subject3_marks = int(input("Enter marks : "))
student[subject3] = subject3_marks

print(student)
print("Length : ", len(student))

"""
# OR

"""

marks = {}

x = int(input("Enter phy marks : "))
marks.update({"phy": x})

y = int(input("Enter eng marks : "))
marks.update({"eng": y})

z = int(input("Enter phy marks : "))
marks.update({"mth": z})


print(marks)

"""

# Practice_04
# Figure out a way to store 9 & 9.0 as seperate value in the set. You can take hep of built-in data types

""" 

set = {9, 9.0}
print(set)  # store only 9

# One possible solution is make the second element string.

set2 = {9, "9.0"}
print(set2)

# Second Solution is Store the values as tuple

set3 = {("float", 9.0), ("int", 9)}
print(set3)

"""
