# file: magic4.py
# The magic number guessing game.

print("You win if you guess the magic number.")
n = int(input("Enter a number: "))
while n != 3:
   if n == 7:
      print("Some people think so, but not me.")
   print("Better luck next time.")
   if n < 3:
      print("Try higher.")
   else:
      print("Try lower.")
   n = int(input("Enter a number: "))
print("You win!")
print("It is the first odd prime. Yay!")
