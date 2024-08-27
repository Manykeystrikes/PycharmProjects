#elseScript.py
#Ask for a number from the user
#If the number is 7, the user wins

print("You win if you guess the magic number.")
num = int(input("Guess the number: "))
if (num == 7):
    print("Congratulations! You win!")
    print("Lucky number 7!")
else:
    print("Wrong number.")
    print("Thank you for playing! Better luck next time!")
