# Practice 01
# Create function find average of 3 numbers
"""
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print("Average of 3 numbers:", avg)
    return avg
calc_avg(55, 32, 99)
"""

# Practice 02
# WAF to print the length of a list. (list is the parameter)
"""
cities = ["A", "B", "C", "D", "E"]
def list_len(x=[]):
    print("length = ", len(x))
    return len(x)
list_len(cities)
"""

# Practice 03
# WAP to print the elements of a list in a single line.(list is the parameter)
"""
aplha = ["A", "B", "C", "D", "E"]
def display(x):
    for ele in x:
        print(ele, end=" ")
    return 0
display(aplha)
"""

# Similar Example Using range()
"""
def display_nums():
    x = range(2, 10)
    for ele in x:
        print(ele, end=" ")
display_nums()
"""

# Practice 04
# WAP to find the factorial of n. {n is the parameter}
"""
number = int(input("Enter a number:"))
def calc_fact(num):
    fact = 1
    while num >= 1:
        fact *= num
        num -= 1
    return fact
output = calc_fact(number)
print("Factorial of", number, "is", output)
"""

# Similar Practice
"""
number = int(input("Enter a number: "))
def calc_facto(number=0):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact
output = calc_facto(number)
print("Factorail of", number, "=", output)
"""

# Practice 05
# WAP to convert USD to PKR
"""
usd_val = int(input("Enter USD's: "))
def convert_curr(currency):
    pkr_val = currency * 158
    print(usd_val, "USD =", pkr_val, "PKR")
convert_curr(usd_val)
"""

# Practice 06
# WAP to take input from user and return wheter it is ODD or EVEN
"""
number = int(input("Enter a number: "))
def check_num(number):
    if number % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
check_num(number)
"""

# Practice 06
# Guess the number using recursion.
"""
guess_num = input("Guess The number: ")
def check_num(x):
    if x == "5":
        print("Correct")
        return
    return check_num(input("Try Again: "))


check_num(guess_num)
"""

# Practice 07
# Write a recursive function to calculate the factorial of a number x
"""
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return factorial(x - 1) * x


print(factorial(10))
"""

# Practice 07
# Write a recursive function to find the sum of the digits of a number.
"""
def sum(n):
    if n == 0:
        return 0
    return sum(n - 1) + n
        
print(sum(15))
"""

# Practice 08
# Write a recursive function to print all elements in a list.
"""
my_list = ["Apple", "Banana", "Candy", "Dinner", "Elephant", "Fruit", "Golf", "Hello"]

def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx], end=" ")
    print_list(list, idx + 1)

print_list(my_list)
"""