'''Problem:
Prompt for and read a string.
Print the number of characters in the string that are decimal digits.
Enter a string: To do: 1. Party like it’s 1999.
Number of digits = 5
Problem: Previously we computed the average of a class’s test
marks using a while loop and the sentinel pattern to read the
marks.
Write a new program that instead of using a negative number
to end input, asks how many marks there are first, then reads
them using a for loop.'''

 # calc avg needed so need mark and total
n = int(input("How many marks: ",))
if n > 0: # n = int(input("How many marks: ",)) - (if) lets the loop continue only if (n) is > 0
   mark = float(input("Enter a mark: ", ))
   highest = mark
   lowest = mark
   total = mark
   while mark <= 0.0:
   for i in range (n - 1): # does a loop a required number of times
      mark = float(input("Enter a mark: ",))
      total += mark
      if mark > highest:
        highest = mark
      if mark < lowest:
        lowest = mark
   print("The number of marks: ", n)
   print("The average mark: ", total / n)
   print("The highest mark: ", highest)
   print("The lowest mark: ", lowest)





# n = 0
# total = 0.0
# mark = float(input("Enter a mark: ",))
# highest = mark
# lowest = mark
# while mark >= 0.0:
#    n += 1
#    total += mark
#    if mark > highest:
#        highest = mark
#    if mark < lowest:
#        lowest = mark
#    mark = float(input("Enter a mark: ", ))
# print("The number of marks: ", n)
# if n > 0:
# print(f"The average mark is: {round(total / n, 2)}")

