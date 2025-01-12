# Chapter 07
# File I/O in Python
"""
Python can be used to perform operation on a file, (read & write data etc).

Types of files:

1: Text Files : .txt, .docx, .log etc.  (data is stored in character form)
2: Binary File: .mp4, .mov, .png, .jpeg etc. (data is stored in any other form instead of character)
"""

# Open, Read & Close File
"""
We have to open a file before reading or writing it.

SYNTAX:

f = open("file_name", "mode")
By Default Mode is set to read.

file_name = "sample.txt or demo.docx"
mode = r: read, w: write

Example: 
data = f.read()
f.close()
"""

# Different Modes

"""
r: open for reading. (default)
w: open for writing, truncating the file first. (truncating means overwrite. first all the data of file will be deleted then you can write your data.)
x: create a new file and open it for writing.
a: open for writing, appending to the end of the file if it exists.
b: binary mode.
t: text mode. (default)
+: open a disk file for updating. (reading and writing)
r+: read & overwriting the existing data & (pointer start).
w+: read & overwrite & data is truncated.
a+: read & append & no truncated & pointer End.  
"""

# Example
"""
txt_file = open("demo.txt", "rt")
data = txt_file.read()  # read("Number of characters")

print(data)
print(type(data))
print(len(data))
txt_file.close()

# Reading first line from demo.txt
txt_file = open("demo.txt", "r")
first_line = txt_file.readline()  # read first line
print(first_line)
txt_file.close()

# .readlines method  ( return multiple lines into list format )
txt_file = open("demo.txt", "r")
mul_lines = txt_file.readlines()
print(mul_lines)
txt_file.close()
"""

# Writing to a file

txt_file = open("demo.txt", "w")
txt_file.write("My name is Danyal.")
txt_file.close()

txt_file = open("demo.txt", "r")
print(txt_file.read())
txt_file.close()

#  Appending Text at the end.

txt_file = open("demo.txt", "a")
txt_file.write("\nCurrently learning python")
txt_file.close()

# Creating a new file

new_file = open("new_file.txt", "w")
new_file.write("Hello Again!")
new_file.close()

# r+ mode

new_file = open("new_file.txt", "r+")
new_file.write("Testing")
print(new_file.read())
new_file.close()
