# forLoop7.py
# changing grade example using for loop

#determine how many grades will be entered 
gradeNumber = int(input("How many grades will be entered: "))
total = 0 #sum of the grades

#using the for loop
for i in range(gradeNumber):  #is this correct?
	grade = float(input("Enter a grade: "))
	total += grade
	
print("Number of grades: ", gradeNumber)
print("Grade average: ", (total/gradeNumber))
