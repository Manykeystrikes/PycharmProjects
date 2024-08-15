'''Test Results
Problem: Prompt for and read marks for a test until a negative
number is entered (which can not be a valid mark). Print the
number of marks entered and the average (arithmetic mean) of
the marks.
Problem: Extend the problem so that it prints out the highest
and lowest marks as well.'''

n = 0
total = 0
mark = float(input("Enter a mark: "))
while mark >= 0.0:
   n += 1
   total += mark
   mark = float(input("Enter a mark: "))

print("Marks recieved: ",n)
if n > 0:
   print("The average mark is: ", total / n)
