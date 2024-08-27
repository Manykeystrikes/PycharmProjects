# illustrate usage of pass statement

numbers = [0, 1, 2, 3]

for n in numbers:
	if (not n):
		pass #do nothing if n is 0
	else:
		n += 2  
	print(n)  #print the result