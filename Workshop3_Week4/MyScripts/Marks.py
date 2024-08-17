#Average Mark

'''Test Results
Problem: Prompt for and read marks for a test until a negative
number is entered (which can not be a valid mark). Print the
number of marks entered and the average (arithmetic mean) of
the marks.
Problem: Extend the problem so that it prints out the highest
and lowest marks as well.'''

n = 0
total = 0.0
mark = float(input("Enter a mark: ",))
highest = mark
lowest = mark
while mark >= 0.0:
   n += 1
   total += mark
   if mark > highest:
       highest = mark
   if mark < lowest:
       lowest = mark
   mark = float(input("Enter a mark: ", ))
print("The number of marks: ", n)
if n > 0:
   print(f"The average mark is: {round(total / n, 2)}")