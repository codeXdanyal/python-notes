# Recursion
# When a function calls itself repeatedly.
# Loops and recursion are interrelated, meaning that tasks done using loops can also be accomplished with recursion
# Base Case: The condition inder which the function stops calling itself.
# without a base case the recursion would go on forever and cause a stack overflow.


# Recursive function
def show(n):
    if n == 0:
        return
    print(n)
    show(n - 1)


show(5)

# Output
"""
show(n=5)   5
show(n=4)   4
show(n=3)   3
show(n=2)   2
show(n=1)   1
show(n=0)   0 
"""

