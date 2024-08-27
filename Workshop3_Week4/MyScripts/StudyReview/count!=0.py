number = int(input("Enter a number(zero to end): "))
positive_count = 0  # the positive count is initialised
while number != 0:
    if number > 0:
        positive_count += 1  # positive_count = positive_count + 1
    number = int(input("Enter a number(zero to end): "))

print(positive_count, "positive numbers were entered.")