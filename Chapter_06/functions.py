# Functions
"""
- Block of statememt that perform specific task.
- Take input(parameter)---->perform calculation----->return output
- Decrease Reduntancy

# Syntax

def func_name(param1,param2...):     #Function defintion
    Some Work
    return val
    
func_name(arg1, arg2..)    #Function call
"""


# Example
# Function Definiton
def sum(a, b):
    sum = a + b
    print(sum)
    return sum


# Function call
sum(5, 2)  # 5 & 2 are arguments
sum(3, 2)
sum(9, 9)


def greet():
    print("Hello")


x = greet()
print(x)

# Built in Functions
# Pre define by  Python
"""
print("danyal", end=" \t")
print("khan")
len()
type()
range()
"""

# User Defined Functions
# Created by US.


# Default Parameters
# default parameter starts from right side
def calc_product(a=0, b=0):
    print(a * b)


calc_product()


# def add_nums(a=3, b): #give us error bcz defaults values start from right sdie
