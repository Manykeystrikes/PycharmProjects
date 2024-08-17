#Problem 1 
'''Problem: The grades at a university are awarded based on the marks awarded for the course out of 100.
Marks of 85 or above receive the grade of 7. 
Marks less than 85 but that are 75 or above receive the grade of 6.
Marks less than 75 but that are 65 or above receive the grade of 5.
Marks less than 65 but that are 50 or above receive the grade of 4.
Anything less than 50 gets the grade of F. Write a program
that asks the user to input the marks and prints the grade awarded
Example:
How many marks? 85
Grade awarded: 7'''

#get input marks
marks = float(input("Enter marks: "))


#transfer marks to a grade
#Marks 85 or above receive the grade of 7
if marks >= 85:
   grade = '7'
# Marks less then 85 but are 75 or above receive the grade of 6
# elif marks < 85 and marks >=: #75 <= marks < 85
elif marks >= 75:
   grade = '6'
#Marks less than 75 but that are 65 or above receive the grade of 4.
elif marks >= 65:
   grade = '5'
#Marks less than 65 but that are 50 or above receive the grade of 4.
elif marks >= 50:
   grade = '4'
#nything less than 50 gets the grade of F. Write a program
else: grade = 'F'
# print grade
print("grade = ", grade)