"""We’ll say that a lowercase ’g’ in a string is ”happy” if there is another ’g’ immediately to its
left or right. Write a function to print ‘HAPPY’ if all the g’s in the given string are happy, otherwise,
print ‘LONELY"""

xs = "234"
def sort(Happy):
    """Sort list xs in place into non-descending order."""
   for i in range(0, len(xs) - 1):
       for j in range(i + 1, len(xs)):
           if xs[j] < xs[i]:


               xs[j], xs[i] = xs[i], xs[j]

x = "xxggt"

if 'g' not in x:
    print('LONELY')
else:
    is_happy = True
    for i in range(len(x)):
        if x[i] == 'g':
