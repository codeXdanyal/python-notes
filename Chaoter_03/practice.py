################## Practice 01 ##################

# WAP to ask the user to enter names of thier 3 facorite movies & store them in a list.

"""
movies = []
mov1 = input("Enter 1st movie : ")
mov2 = input("Enter 2nd movie : ")
mov3 = input("Enter 3rd movie : ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

"""

# Second way

"""

movies = []
mov1 = input("Enter 1st movie : ")
movies.append(mov1)
mov1 = input("Enter snd movie : ")
movies.append(mov1)
mov1 = input("Enter 3rd movie : ")
movies.append(mov1)

print(movies)

"""
# Third way

"""
movies = []
movies.append(input("Enter 1st movie : "))
movies.append(input("Enter 2nd movie : "))
movies.append(input("Enter third movie : "))

print(movies)

"""

# Fourth way

"""

user  = input("Enter your favorite movies : ")
list = user.split()

print(list)
print(len(list))

"""

################## Practice 02 ##################

# WAP to check of a list contain a palindrome of elemens, use copy() method

"""

list1 = [1,2,3,4,5,6]
list2 = [6,5,4,3,2,1]

copy = list1.copy()
copy.reverse()
if(copy == list2):
    print("Palindrome")
else:
    print("Not Palindrome")    

"""

################## Practice 02 ##################

# WAP to count the numner of students with the "A" grade of the following tuple

"""

grades = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
print(grades.count("A"))

"""
# Store the above values in a list & sort them in ascending order

"""
grades_list = list(grades)
grades_list.sort()
print(grades_list)

"""

