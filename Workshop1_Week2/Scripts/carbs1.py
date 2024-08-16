# file: carbs1.py
# Calculate the molecular weight of any carbohydrate.

# atomic weights
H = 1.00784
C = 12.0096
O = 15.99903

h = int(input("How many atoms of H: "))
c = int(input("How many atoms of C: "))
o = int(input("How many atoms of O: "))
print("Molecular weight =", h * H + c * C + o * O)


