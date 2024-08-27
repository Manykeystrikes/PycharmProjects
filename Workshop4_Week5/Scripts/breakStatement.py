# breakStatement.py
# illustrate usage of break statement

numbers = [0, 1, 2, 3]

for n in numbers:
	if (n == 1):  #if (not n):
		break
	else:
		n += 2  
	print(n)  #print the result
