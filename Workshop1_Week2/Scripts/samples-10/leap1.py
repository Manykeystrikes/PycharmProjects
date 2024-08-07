# file: leap1.py
# Is a year a leap year?

y = int(input("What year? "))
isLeap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
print("Is it a leap year?", isLeap)
