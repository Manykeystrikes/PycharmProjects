#Problem: 4
'''Problem: A car dealer earns a base wage of $36.25 per hour up to their normal work week of 37 hours.
Only whole hours are counted. If he works more hours than that (overtime) he gets paid at 1.5 times his
normal rate for the overtime. If he sells more than 5 cars in a week, he gets a bonus of $200 per car from
the 6th car sold. Write a program that takes as input the number of hours worked and the total number
of cars sold for the week, and outputs the car dealer’s total salary for the week.
Examples:
How many hours were worked? 41
Total number of cars sold for the week? 10
The salary is 2558.75
How many hours were worked? 36
Total number of cars sold for the week? 3
The salary is 1305.0
Testing: Test your program by checking the output for the following two scenarios:
 Hours worked: 25; Number of cars sold: 10
 Hours worked: 40; Number of cars sold: 5
Have you checked whether valid values are provided?'''
# User to input units realted to request
hours = float(input("How many hours were worked? "))
cars_sold = float(input("number of cars sold per week "))
#work out the hrs worked
if hours <= 37:
    wage = 36.25
elif hours > 37:
    wage = 36.25 * 1.5
if cars_sold > 5:
    bonus = ( cars_sold -5) * 200
else: bonus = 0

total_salary = (wage * hours) + cars_sold + bonus
print("Your total salary is ", total_salary)

