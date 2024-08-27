# script: function3.py
# Declare and call a function:
#   with multiple arguments, and a return value

def finalBalance(p, r, n):
   """Returns a final balance with compound interest.
   
      p in the principle (initial balance)
      r is the interest rate per term
      n is the number of terms"""
   return p * (1.0 + r) ** n
   
initBal = float(input("Initial balance: "))
annRatePct = float(input("Annual interest rate (%): "))
months =  int(input("Number on months: "))
finalBal = finalBalance(initBal, 
             annRatePct / 100.0 / 12.0, months)
print("Final balance = ${:.2f}".format(finalBal))
