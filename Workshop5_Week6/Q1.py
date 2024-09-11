cost = float(input("Enter the cost: ",))
diff = 100.0 - cost
if cost <= 100:
   discount = 0.0
   print("You do not qualify yest for the discount", diff)
elif 100 >= cost < 200:
   discount = 0.1
elif 200 >= cost < 250:
   discount = .10
elif 250 >= cost < 300:
   discount = .15

cost = cost * (1 - discount)
print(f"Cost including discount, ${cost}")