'''Problem: In mathematics, the Fibonacci sequence is defined such that each Fibonacci number is the
sum of the two preceding ones, starting from 0 and 1. That is,
F1 = 0, F2 = 1, F3 = 1, F4 = 2, ..., Fn = F(n-1) + F(n-2).
Write a program that given an input n, outputs the first n Fibonacci numbers. The format of output is
that at most 4 numbers can be displayed in a row.
Example run:
Enter a positive number: 6
0 1 1 2
3 5
Enter a positive number: 10
0 1 1 2
3 5 8 13
21 34
Testing: Test your code for the above example input.
'''
def fibonacci(n): 0
a = 0
b = 1
n = int(input("Enter a positive number: "))
result = []
for i in range(n):
    (a, b) = 0, 1
   # while a < n:
    result.append(a)
    a, b = b, a + b
     #if n < 0:
   print("Please enter a positive number")
print(a, end=" ")

   # n = int(input("Enter a positive number: "))
    #print("Fibonacci number: ", a)


    #Fn = F(n - 1) + F(n - 2)

