# script: function4.py
# Declare and call a function:
#   with multiple arguments, some keyworded

def printBox(width, height, empty = False, framed = False):
   """Print a patterned  box of size width x height
      characters."""
   for i in range(height):
      for j in range(width):
         if framed and \
            (i == 0 and (j == 0 or j == width - 1) or \
            i == height - 1 and (j == 0 or j == width - 1)):
            print("+", end = "")
         elif framed and (i == 0 or i == height - 1):
            print("-", end = "")
         elif framed and (j == 0 or j == width - 1):
            print("|", end = "")
         elif not empty and (i + j) % 2 == 0:
            print("X", end = "")
         elif not empty:
            print("O", end = "")
         else:
            print(" ", end = "")
      print()
   
printBox(5, 3)
printBox(10, 4, framed = True)
printBox(10, 4, framed = True, empty = True)


