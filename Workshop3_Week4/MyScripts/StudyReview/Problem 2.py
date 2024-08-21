#2.2 Problem 2
'''Problem: A shipping company charges its customer based on the weight of goods and the distance of
shipping. A discount is given based on the distance of shipping as follows:
distance < 250km, no discount
250km ≤ distance < 500km, 10% discount
500km ≤ distance < 1000km, 15% discount
1000km ≤ distance < 2000km, 20% discount
2000km ≤ distance < 3000km, 35% discount
3000km ≤ distance, 50% discount
The shipping cost is calculated based on the following equation:
cost = basePrice * weight * distance * (1 - discount).
Write a program that takes as inputs the base price, weight, and distance, and prints the shipping cost to be
charged to the customer.
Example:
How much is the base price? 0.01
What is the weight? 200
What is the distance? 1000
The shipping cost is 1600.0
Testing: Test your program by checking the output for the following two scenarios:
 Base price: 0.1; Weight: 540; Distance: 2300
 Base price: 0.35; Weight: 350.5; Distance: 734.5'''

weight =float(input("What is the weight? ",))
distance = float(input("What is the distance? ",))
price = float(input("How much is the base price? ",))

if distance < 250:
   discount = 0.0
elif 250 >= distance < 500:
   discount = 0.10
elif 500 >= distance < 1000:
   discount = 0.15
elif 1000 >= distance <2000:
   discount = 0.20
elif 2000 >= distance <3000:
   discount = 0.35
if distance > 3000:
   discount = 0.50
    
cost = (weight * distance * price) *( 1 - discount)
print(f"The shipping cost= ${round(cost ,2)}")
 