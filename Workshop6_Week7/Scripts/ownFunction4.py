#define function with parameters and returning value 
def finalBalance(d, c):
	""" returns the final balance after applying a discount	

	d is the discount that should be applied as a percentage
	c is the cost before applying the discount"""
	d = d/100 #convert to percentage
	discountedValue = c - (d*c)
	return discountedValue

#calling function
finalBalance(10, 120)
b = finalBalance(20, 200)
print(b)
print(finalBalance(20, 200))