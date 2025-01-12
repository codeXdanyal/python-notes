# Without 'with' syntax
"""
f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()
"""

# With syntax

with open("demo.txt", "r+") as f:
    f.write("\nMy name is Danyal. Currently learning Python from apna college")


# Practice

# Append the text at end
with open("sample.txt", "a+") as f:
    f.write("\nWait...")

# Read the file from staring.
with open("sample.txt", "r+") as f:
    print(f.read())

# Overwrite the file
with open("sample.txt", "w+") as f:
    f.write("Wait...")
