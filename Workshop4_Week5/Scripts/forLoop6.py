# forLoop6.py

#prompt user for string
userString = input("Enter a string: ")

#what will we use here as sequence?
num = 0
for s in userString:
	#what will we check for?
	if (type(s) == 'int'):  #will this work?
		num += 1
print("Number of digits in string, ", userString, ": ", num)
