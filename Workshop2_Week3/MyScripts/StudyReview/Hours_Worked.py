Problem: A programmer would like to calculate the hourly wage of a job. Write a program that asks the
user for the number of hours worked per day, number of days worked in a week, and the annual salary.
Calculate and print the programmer’s hourly wage with the assumption that there are 52 weeks in a year.
For example, the output should look like this when the program is run:
Number of hours worked per day: 7.5
Number of days worked in a week: 5
Annual salary: 60000
Hourly wage = $30.76923076923077
Testing: Test your program by checking the output for the following two scenarios:
 Number of hours worked per day: 8; Number of days worked in a week: 3; Annual salary: 89920.15
 Number of hours worked per day: 5; Number of days worked in a week: 5; Annual salary: 493

Weeks_Per_Year = 52

Daily_Hours_Worked = float(input("Number of hours worked per day: ",))
Days_worked_perWeek = float(input("Number of days worked in a week: ",))
Annual_Salary = float =(input("Annual Salary: ",))



 total_hours = (Daily_Hours_Worked * Days_worked_perWeek)
 
 hourly_wage = (total_hours * Weeks_Per_Year)
 
 print(f"Hourly Salary= ${round(hourly_wage, 2)}")
 