#find the middle character of a string

def middleChar(s):
    """returns the character at the middle of a string
    
        Precondition: len(s) > 0
        Postcondition: returns the character at the least position closest to 
        the middle of s """
    
    return s[len(s)//2]


s1 = input("Enter a string: ")
m = middleChar(s1)
print("The middle character of", s1, "is", m)

