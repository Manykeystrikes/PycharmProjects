#sort list in descending order
def descendingOrder(myList):
    """sort the list in descending order"""

    for i in range(0, len(myList)-1):
        for j in range(i+1, len(myList)):
            #compare the elements
            if (myList[j] > myList[i]):
                #swap elements
                #assign one value to temp, assign the value to swap, assign the temp 
                myList[i], myList[j] = myList[j], myList[i]

l = [20, 2, 40, 5, 40]
print(l)
descendingOrder(l)
print(l)

