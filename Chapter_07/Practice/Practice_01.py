# Practice_01

# Create a new file "practice.txt" using python.Add the following data in it:
"""
Hi everyone
we are learning File I/O
using java
I like programming in java.
"""

#  WAF that replace all occurence of "java" with "python" in above file
"""
with open("practice.txt", "w+") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using java\nI like programming in java.")

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")

with open("practice.txt", "w") as f:
    f.write(new_data)
"""

# Practice 02
# WAF to Search if the word "learning" exist in the file or not.
"""
def find_word(x):
    if data.find(x) != -1:
        output = "Found"
    else:
        output = "Not Found"
    return output

with open("practice.txt", "r") as f:
    data = f.read()
    print(find_word("learning"))
"""


# Practice 03
# WAF to find in which line of the file does the word "learning" occur first. Prinf -1 if word not found.
"""
def check_for_line():
    word = "learning"
    data = True
    line = 1
    with open("practice.txt", "r") as f:
        while data:
            x = f.readline()
            if word in x:
                print("Found on line :", line)
                return            
            line += 1
            
check_for_line()
"""

