#sentinel pattern
#read first value

grade = float(input("Enter your grade: "))
print("Enter negative value to stop! ", )
sum = 0
count = 0
while grade >= 0:
    sum = sum + grade
    count += 1
    grade = float(input("Enter your grade: "))

if count != 0:
   avg = sum / count
else:
    avg = 0

print("Your average grade is: ", avg)


