#have stock of pens and books
#customer can request to order pens and books
#if not enough stock, need to ask if they want what is left, if yes update stock
#if five or less are left of any one item, print a message to order new stock
#stop when both the requested number of pens and books are zero

#get user input
pensRequested = input("Number of pens requested to be purchased:")
booksRequested = input("Number of books requested to be purchased:")

#while loop, using sentinel patter
#stop when both values are zero
while (pensRequested != 0) and (booksRequested != 0):   #stop if (pensRequested == 0) and (booksRequested == 0)
    #process the data

    #get new input
    pensRequested = int(input("Number of pens requested to be purchased:"))
    c1 = pensRequested != 0
booksRequested = int(input("Number of books requested to be purchased:"))
c2 = booksRequested != 0
print("c1 = ", c1)
print("c2 = ", c2)
    
