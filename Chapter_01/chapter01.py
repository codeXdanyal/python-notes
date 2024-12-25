############################ First Program ################################
print("Hello World")

############################ Variables ################################
name = "Danyal"  # String
age = 20  # Integer Number
price = 22.22  # Floating point number
age2 = age  # age2 value will be 20
variable1 = "valid varibale name"

print("My Name is", name)
print("My age is", age)

# 1variable  is not valid identifier/variable name
# special character are not allowed in our identifier

# Checking Data Type of identifier by type function
# Python automatically detect data type of identifier

print(type(name))  # String
print(type(age))  # int
print(type(price))  # float


############################ Data Types ################################
# Integer    Positive, Nagitive, 0
# String     " Double Quote ", 'Single Quotes', '''Triple QUote''''
# Float      Decimal Values   22.4, 3.99, 9.22
# Boolean    True False   Capital T & F
# None       Not storing any value yet

# Example
age = 23
old = False
a = None

print(type(age), age)
print(type(old), old)
print(type(a), a)

############################ Keywords ################################
# Keywords are reserved words in python
# and, as, break, class, def, False, return, lambda, try etc

# Practice
# Print SUM Of two numbers

x = 10
y = 20
sum = x + y
sub = x - y
mul = x * y
div = x / y
floorDiv = x // y
print(sum)
print(sub)
print(mul)
print(div)
print(floorDiv, "floor division")

############################ Tokens ################################
# Tokens are the smallest units of meaningful data in a program that the interpreter or compiler can recognize.
# Keywords, Identifiers, literals, Operators, Delimeter
# Punctuators
# Punctuators are symbols to orginize sentence structure in programming
# punctuators are symbols use to roginize the sentence structure

# (),{},@,[],# etc
#  -=, +=, /=, *=, //==, = etc

############################ Expression Execution ################################

# String & Numeric valuess can operate together with *
a, b = 2, 3
txt = "@"
print(2 * txt * 3)  # output @@@@@@  --> 6 time

# String & String can operate with + ( Concatenation )
c, d = "2", 3
text = "@"
print((c + text) * d)  # output 2@2@2@

num1 = "hello"
num2 = "2"
sum = num2 + num1
print(sum)
