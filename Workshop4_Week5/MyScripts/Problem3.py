# Problem1
'''roblem 3
Problem: A palindrome is a number or a text phrase that reads the same backwards as well as forwards.
Examples of palindromes are 123321, 1234321, 55555, 22, 454, 1, 0. Write a program that reads in a
positive integer number and prints out whether that number is a palindrome.
Example run:
Enter a positive number: 12321
12321 is a palindrome
Enter a positive number: 1234
1234 is not a palindrome
Testing: Test your code for the example input shown above.
Well done for finishing these activities!
'''



x = "abcdefg"

reverse_x = ""
print=int(input("Enter a positive number: "))
for letter in x:
    reverse_x += letter + reverse_x
print(reverse_x)
    #reverse_x = reverse_x[::-1]
    #print(letter, reverse_x)
#if letter == x[-1]:




