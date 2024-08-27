# continueStatement.py
# illustrate usage of continue statement

numbers = [0, 1, 2, 3]

for n in numbers:
	if (not n):
		continue  #exits body of loop, skips to next iteration
	else:
		n += 2  
	print(n)  #print the result
