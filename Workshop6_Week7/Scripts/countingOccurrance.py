def occurrence(aList, aValue):
    """returning the number of times a value occurs within a list"""

    count = 0
    for i in range(0, len(aList)):
        if (i==aValue):  #what is wrong here?
            count += 1

    return count


s = [1, 30, 5, 88]
print(occurrence(s, 30))

s = [1, 30, 5, 88]
print(occurrence(s, 3))

s = [1, 30, 5, 88, 30, 6, -30]
print(occurrence(s, 30))

s = [1, 30, 5, 'hello', 88, 'hi', 30, 6, -30]
print(occurrence(s, 'hello'))