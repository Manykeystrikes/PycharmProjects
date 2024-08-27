# averageGrade.py - calculates the average grade

#sentinel pattern
#read first value
grade = float(input("Enter a grade (negative value to stop): "))
#check value against condition – not sentinel value

sum = 0
num = 0
while (grade >= 0):
#repeat the following statements
	#what do we do with value?   
	#why here? why not after reading?
	sum += grade
	num += 1
	#read next value
	grade = float(input("Enter a grade (negative value to stop): "))

#print out results (number of grades entered and average)
print("Number of grades: ", num)
print("Average grade: ", sum/num)
