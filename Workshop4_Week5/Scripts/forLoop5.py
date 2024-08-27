# forLoop5.py

#prompt user for number of rows and columns
rows = int(input("Number of rows: "))
columns = int(input("Number of columns: "))

#what will we use here as sequence?
for r in range(1, rows):  #why start with 1?
	for c in range(1, columns):
		#print (r, “ “, c)  #printing out the values of r and c
		print("#")
	print() #print a new line after each row

#why is it not printing correctly?