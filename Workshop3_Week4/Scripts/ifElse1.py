# file: ifElse1.py
# Actions and alternatives.

print("You win if you guess the magic number.")
n = int(input("Enter a number: "))
if n == 3:
   print("You win!")
   print("It is the first odd prime. Yay!")
else:
   print("Sorry.")
   print("Better luck next time.")
