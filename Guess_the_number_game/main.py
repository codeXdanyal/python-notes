# Guess the number game
import random

target = random.randint(1, 20)

while True:
    userChoice = input("Guess the target between 1 & 20 or Quit: ").strip()
    if userChoice.lower() == "quit":
        break
    elif not userChoice.isdigit():
        print("Invalid input! Please enter a number between 1 and 20.")
        continue

    userChoice = int(userChoice)
    
    if userChoice == target:
        print("Success : Correct Guess!! 🎉")
        break
    elif userChoice < target:
        print("your number was too small. Take a bigger guess..")
    elif userChoice > target:
        print("your number was too big. Take a smaller guess..")


print("------Game over-----------")
