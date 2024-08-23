''' MarksReceived.py
Prompt for and read marks for a test until a negative number is enterd
(which cannot be a vaild mark). Print the number of marks entered and 
the average (arithmetic mean) of the marks, and the lowest and 
the highest marks'''

n = 0
total = 0.0
mark = float(input("Enter a mark:"))
highest = mark
lowest = mark
while mark >= 0.0:

   n += 1
   total += mark
   if mark > highest:
      highest = mark
   elif mark < lowest:
      lowest = mark
   mark = float(input("Enter a mark:"))
print("The number of marks: ", n)
if n > 0:
   print(f"The average mark is=  {round( total / n, 2)}")
   print("The lowest mark is= ", lowest)
   print("The highest mark is= ", highest)
   