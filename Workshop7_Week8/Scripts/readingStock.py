#we have a file from our stock provider what has been delivered to us after ordering from them
#we want to read in stock items from the file and update the stock count for each item

#ask for file name from user
stockFileName = input("Enter the stock file name:")
stock = []  #list of my stock

try:

    #open the file
    stockFile = open(stockFileName)

    for line in stockFile:        
        print(line, end="")

    
    #close the file
    stockFile.close()
except:
    print("The file", stockFileName, "does not exist")