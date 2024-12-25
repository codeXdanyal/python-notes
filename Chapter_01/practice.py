# # #################### Practice 01 #########################

"""
1) /* is a symbol used in Python for single line comment.
2) 2ndNAme is an invalid identifier in Python.
3) ** is a valid arithmetic operator in Python.
4) in is a logical operator in Python.
5) Variable declaration is implicit in Python.

Solution:
1) False
2) True
3) True
4) False
5) True
"""

# #################### Practice 02 #########################

# # # Consider the given expression:

"""
not True and False or True
Which of the following will be correct output if the given expression is evaluated?   
(a) True
(b) False
(c) NONE
(d) NULL  

Solution:
Starts from left side
not true = false
false and false = false
fasle or true = true
So final answer is True
 """

# # #################### Practice 03 #########################

# # # Traffic lights

"""
light = input("Light is: ")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("ready")
elif(light == "green"):
    print("Go")
else:
    print("Light is broken")

"""

# # #################### Practice 04 #########################

# # #  Grades of students

"""
marks = int(input("Enter Your Marks: "))
grade = ""

if(marks >= 90 and marks <= 100):
    grade = "A"
elif(marks >= 80 and marks <= 89):
    grade = "B"
elif(marks >= 70 and marks <= 89):
    grade = "C"
elif(marks >= 60 and marks <= 89):
     grade = "D"
elif(marks >= 50 and marks <= 89):
    grade = "E"
elif(marks >= 0 and marks <= 89):
    grade = "F"
else:
    print("Enter valid marks")    
   
print("According to your marks your grade is",grade) 
 
 """

# # #################### Practice 05 #########################

# # #  print ouptut for

"""
# A = 5,  g = "M"

A = int(input("A: "))
G = input("M/F : ")

if ((A == 1 or A == 2) and G == "M"):
    print("Fee is 100")
elif((A == 3 or A == 4) or G == "F"):
    print("Fee is 200")
elif((A == 5 or A == 6) and G == "M"):
    print("Fee is 300")
else:
    print("No Fees")
  
"""
# # #################### Practice 06 #########################
"""
 food = input("ENter Food Name: ")
 eat = print("Yes") if food == "spple" else print("No")
 print(eat)
"""
# # #################### Practice 07 #########################

"""
food = input("Food: ")
print("Sweet") if food == "mange" or food == "cake" else print("Not Sweet")
"""
# # #################### Practice 07 #########################

# # #  Clever Ternary Operator

"""
age = int(input("Enter your age: "))
result = ("Your CANNOT Vote", "You CAN Vote") [age >= 18]
print(result)

"""

# # #################### Practice 08 #########################

# # # Tax calculator

"""
sal = float(input("Enter Your Sal: "))
tax = sal*(0.1, 0.2) [sal >= 50000]
print("TAX = ", tax)

"""
# # #################### Practice 09 #########################

# # # calculate interest

"""
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
print(a*b*c/100)

# Improved

m = float(input("m: "))
n = float(input("n: "))
o = float(input("o: "))
output = (a*b*c)/100
print(output)

"""

# # #################### Practice 10 #########################
# #  Input Function

"""

name = input("Enter your name: ")
print("Welcome", (name + " khan ") * 3)

"""

# #################### Practice 11 #########################
# Taking name, age, marks from user

"""
name = input("Enter your name: ")
age = int(input("Age: "))
marks = float(input("Marks: "))

print("Your Name:", name, "| Your Age:", age, "| Your Marks:", marks)

print("typeOF name", type(name), "typeOf Age:", type(age), "typeOf", type(marks))

"""
# #################### Practice 12 #########################

# Checking if user can vote or not

"""
age = int(input("Enter your age : ") ) 

if (age < 18 or age > 60):
    print("You CANNOT Vote")
elif (age >= 18):
    print("You CAN vote")
else:
    print("Invalid input")
    
"""

# #################### Practice 13 #########################

# Write a program to check if number entered by the user is odd or even

"""
number = int(input("Enter a number : "))
if(number %2 == 0):
    print(number, "is even number")
else:
    print(number, "is ODD number")    

"""

# #################### Practice 14 #########################

# Write a program to find the greatest of 3 numbers entered by the user.

"""

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))
greater_num = None

if (num1 >= num2 and num1 >= num3):
    greater_num = num1
elif (num2 >= num3):
    greater_num = num2
else:
    greater_num = num3    

print("Greater Number is : ", greater_num)

"""

# #################### Practice 15 #########################

# Write a program  to check if number is multiple of 7 or not.

"""

number = int(input("enter a number : "))

if (number % 7 == 0): print(number, "is multiple of 7")
else: print(number, "is NOT multiple of 7")

"""
