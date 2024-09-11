
"""Write a program that allows the user to enter two lists of integers, calculate the sum of the
first and the last integers in each list, and print the larger sum. In the event of a tie, print ‘Same’.
When there is only one integer in the list, the sum is the integer itself.
Example input and output:
List 1: 1 2 3 4 5
List 2: 5 6 7
Output: 12
List 1: 4 3 10 1
List 2: 9
Output: 9
List 1: 4 3 2 1
List 2: 1 2 3 4
Output: Same"""
'input for the 2 lists'
list1 = int(input("Enter the first list of integers: "))
list2 = int(input("Enter the first list of integers: "))
'calculate the sum of two lists'
def calculate_sum(lst):
    sum1 = calculate_sum(list1)
    sum2 = calculate_sum(list2)
    sum = list1 + list2
    return sum


if sum1 > sum2:
    print(sum1)
      else: sum2 > sum1:
        print(sum2)
print("Same")
