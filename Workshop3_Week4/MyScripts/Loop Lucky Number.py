'''Loop lucky number
ask for a number form the user
if the number is 7, '''

print("You win if you guess the magic number.")
num = int(input("Guess the number:"))
if(num == 7):
   print("Congratulations! You Win!")
   print("Luck number 7!")
else:
   print("Wong number.")
   print("Thank you for playing! Better luck next time!")