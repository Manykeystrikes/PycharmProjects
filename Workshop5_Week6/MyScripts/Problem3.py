# Problem1
'''Problem: In mathematics, the Fibonacci sequence is defined such that each Fibonacci number is
the sum of the two preceding ones, starting from 0 and 1. That is,
F1 = 0, F2 = 1, F3 = 1, F4 = 2, ..., Fn = F(n-1) + F(n-2).
Write a program that given an input n, outputs the first n Fibonacci numbers.
The format of output is that at most 4 numbers can be displayed in a row.

Example run:
Enter a positive number: 6
0 1 1 2
3 5
Enter a positive number: 10
0 1 1 2
3 5 8 13
21 34'''
i = 1
a = 0
b = 1
n=int(input("Enter a positive number: "))
result = []
#a, b = 0, 1
while a <= n:
      if (i % 4 != 0):  # only allocates upto 4 integers
        result.append(a) # append adds to the list and modifies it
      #sum = a + b
      a, b = b, a + b  # a,b initialised then 0 + 1 = 1; 1 + 2 = 2; 1 + 2 = 3
print(sum) # output prints on same line
      #print(sum) #diplays the output (from the lopping  of the (sum)
print(result) # prints the result








#x = "abcdefg"

#reverse_x = ""



