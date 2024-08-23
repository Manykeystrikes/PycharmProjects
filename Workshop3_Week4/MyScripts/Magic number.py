''' while loop
change magic number example using while loop'''

#user should be guessing until they get the number

correctNumber = 7

num =  int(input("Enter a number: "))

while num != 7:
   if num < 7:
      print("Not the magic number,to small")
   else:
       print("Not the magic number,to large")
   num = int(input("Try again, enter a number: "))
print("Good guess, you got the magic number")
