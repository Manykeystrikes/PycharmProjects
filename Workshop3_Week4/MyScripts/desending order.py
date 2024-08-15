'''Prob 3 Decending order

Problem: Write a program that takes as input 3 integers and outputs them in descending order.
Examples:
Integer 1? 3
Integer 2? 10
Integer 3? 2
Sorted: 10 3 2
Testing: Test your program by checking the output for the following two scenarios:
•	Integer 1: 35; Integer 2: 21: Integer 3: 28
•	Integer 1: 25; Integer 2: 33: Integer 3: 43
'''

## Function to sort three integers in descending order
def sort_descending(a, b, c):#def keyword is used to define a function, it is placed before a function name
    numbers = [a, b, c]
    numbers.sort(reverse=True)
    return numbers

# Taking input from the user
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

# Sorting and displaying the result
sorted_numbers = sort_descending(a, b, c)
print("Numbers in descending ord"
      ""
      "er:", sorted_numbers)