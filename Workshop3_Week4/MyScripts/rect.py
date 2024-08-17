# rect.py
#Print a rect of hashes

'''Solve these problems as a class.
Problem: Prompt for and read a number. Print that many hashes
(#) in a line.
Enter a number: 5
#####
Problem: Prompt for and read numbers of rows and columns.
Print those many rows and columns of hashes.
Enter rows: 2
Enter columns: 5
#####
#####'''



rows = int(input("Enter rows: ",))
cols = int(input("Enter columns: ",))
for j in range(rows):
   for i in range (cols):
      print("#", end= "")
   print()


