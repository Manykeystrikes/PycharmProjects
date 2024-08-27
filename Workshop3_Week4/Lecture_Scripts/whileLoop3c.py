# whileLoop3.py
# changing magic number example using while loop

#user should keep guessing until they get the number correct 
correctNumber = 7
#getting first number from user
num = float(input("Enter a number: "))
#when should we stop the while loop?
while (num !=7):  	
	#print message to user, hint for next guess
	if (num < 7):
		print("Incorrect guess. Number is too small!")
	else: #why only 1 alternative here and not 2?
		print("Incorrect guess. Number is too large!")
	#get next number from user
	num = float(input("Try again! Enter a number: "))	
