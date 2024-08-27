#initial balance
balance = 1000

interest_rate = 0.05 # 5% interest rate
#know what the balance is after number of years
target_balance =5000

#number of years
years = 0
while balance < target_balance: # loop until balance exceeds the target
    #apply the interest to first year
    if years < 3:
        years += 1
        continue
    else:
       balance += interest_rate * balance

    print(f"Years {years}: Balance= ${balance:.2f}.")
    years += 1

print(f"It will take {years} years to reach ${target_balance:.2f}.")
print(f"Final balance after {years} years is ${balance:.2f}.")




