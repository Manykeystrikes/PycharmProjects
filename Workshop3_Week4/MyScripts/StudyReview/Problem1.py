'''Problem: The grades at a university are awarded based on the marks awarded for the course out of 100.
Marks of 85 or above receive the grade of 7. Marks less than 85 but that are 75 or above receive the
grade of 6. Marks less than 75 but that are 65 or above receive the grade of 5. Marks less than 65 but
that are 50 or above receive the grade of 4. Anything less than 50 gets the grade of F. Write a program
that asks the user to input the marks and prints the grade awarded

Marks of 85 or above receive the grade of 7
Marks less than 85 but that are 75 or above receive the grade of 6
Marks less than 75 but that are 65 or above receive the grade of 5
Marks less than 65 but that are 50 or above receive the grade of 4
Anything less than 50 gets the grade of F'''


mark = float(input("Enter a mark: ",))

if mark >= 85:
   grade = 7
elif mark >= 75:
   grade = 6
elif mark >= 65:
   grade = 5
elif mark >= 50:
   grade = 4
else: grade = 'F'


str_grade = str(grade)

print("str_grade = ", grade)


