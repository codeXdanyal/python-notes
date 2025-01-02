# Break & Continue Keyword

# Break: Used to terminate the loop when encountered.
# Continue: Terminate execution in the current iteration & continue execution of the loop with the next iteration.

# Break Example
"""
i = 1
while i <= 5:
    print(i)
    if (i == 3):
        break
    i += 1
    
print("Loop Ended")
"""

# Continue Example

j = 1
while j <= 5:
    if j == 3:
        continue  # Skip
    print(j)
    j += 1
