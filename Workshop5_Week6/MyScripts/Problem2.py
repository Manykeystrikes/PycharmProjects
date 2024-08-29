#Problem2.py
'''Problem: Given an input number n, print a diamond shape with 2*n-1 rows.
Example run:
Enter a positive number: 3
xxx
xxxx
xxxxx
xxxx
xxx
Testing: Test your code for the above example input.'''

'''rows = int(input("Enter rows: ",))
cols = int(input("Enter columns: ",))
for j in range(rows):
   for i in range (cols):
      print("#", end= "")
   print()'''
n = 0
x = 0
i = 0

n = int(input("Enter a number: "))
for i in range( 2, - i, -1):
    print("" * (n - i ), "#" * (2 * i - 1))
#for i in range( 2, - i, +1):
 #   print("" * (n + i), "#" * (2 * i + 1))
    print("#")





