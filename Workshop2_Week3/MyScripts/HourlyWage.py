#CalculteWage


H = 7.5
D = 5
S = 60000
WeeK_in_Year = 52
# cal hrs per year

hours_per_day = float(input("Number of hours worked: ",))
num_days_per_week = int(input("Number of days worked: ",))
ann_salary = float(input("Yearly Salary: ",))



total_hours = hours_per_day * num_days_per_week * WeeK_in_Year

hourly_wage = ann_salary / total_hours

print(f"Hourly wage = ${round(hourly_wage, 2)}")
