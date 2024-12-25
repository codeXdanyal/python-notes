# Ternary Operator

# food = input("ENter Food Name: ")
# eat = print("Yes") if food == "spple" else print("No")
# print(eat)

# -----------------------------------------------------------------------

# food = input("Food: ")
# print("Sweet") if food == "mange" or food == "cake" else print("Not Sweet")

# -----------------------------------------------------------------------

food = input("Enter Sweet Food name: ")
output = ("not sweet", "sweet")[food == "apple"]
print(output)

age = int(input("Enter your age: "))
result = ("Your CANNOT Vote", "You CAN Vote")[age >= 18]
print(result)
