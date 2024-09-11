#we have a file from our stock provider what has been delivered to us after ordering from them
#we want to read in stock items from the file and update the stock count for each item

#ask for file name from user
name = input("Enter the file name: ")

try:
    #open the file
    stockFile = open(name)

    #read in all items from file
    #approach 1 using while and sentinel pattern
    line = stockFile.readline()
    while (line != ""):
        #processing the data
        print(line)

except:
    print("The file", name, "does not exist")


