#have stock of pens and books
#customer can request to order pens and books
#if not enough stock, need to ask if they want what is left, if yes update stock
#if five or less are left of any one item, print a message to order new stock
#stop when both the requested number of pens and books are zero

#get user input
pensRequested = int(input("Number of pens requested to be purchased:"))
booksRequested = int(input("Number of books requested to be purchased:"))

#stop when both the requested number of pens and books are zero
#use sentinel pattern in while loop

#check condition using output
cond = (pensRequested !=0) and (booksRequested !=0)
print(cond)

while (pensRequested !=0) and (booksRequested !=0):
    #process the data

    #get new input
    pensRequested = int(input("Number of pens requested to be purchased:"))
    booksRequested = int(input("Number of books requested to be purchased:"))
    #check condition using output
    cond = (pensRequested !=0) or (booksRequested !=0)
    print(cond)

