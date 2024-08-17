#C:\Users\adbar>python
#Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
coffee = 5.5
coffee
5.5
print(coffee)
5.5
print("The price of coffee = ", coffee)
#The price of coffee =  5.5
print("The price of coffee= ", 5 * coffee)

The price of coffee=  27.5
tea = 3.0
print("The price of tea = ", tea, "The price of coffee= ", coffee)
The price of tea =  3.0 The price of coffee=  5.5
print("The price of tea- ", tea, "The price of coffee= ", coffee, sep"!")
  File "<stdin>", line 1
    print("The price of tea- ", tea, "The price of coffee= ", coffee, sep"!")
                                                                         ^^^
SyntaxError: invalid syntax
print("The price of tea- ", tea, "The price of coffee= ", coffee, sep="!")
The price of tea- !3.0!The price of coffee= !5.5
print("The price of tea = ", tea, "The price of coffee= ", coffee, sep="!", end=".")
The price of tea = !3.0!The price of coffee= !5.5.

print)"The price of tea= ", tea, "The price of coffeee= ", coffee, sep="!", end=".\n")
  File "<stdin>", line 1
    print)"The price of tea= ", tea, "The price of coffeee= ", coffee, sep="!", end=".\n")

print("The price of tea= ", tea, "The price of coffee= ", coffee, sep="!", end=".\n")
The price of tea= !3.0!The price of coffee= !5.5.

 print("The price of tea= ", tea, "The price of coffee= ", coffee, sep="!", end=".\n")
The price of tea= !3.0!The price of coffee= !5.5.
 price  = 5.5
 "The price of coffee = " + price
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "float") to str
 "The price of coffee= " + str(price)
'The price of coffee= 5.5'

 print(52, end=',')
52,
 print(52, end=',\n')
52,
 print(52, sep='!", end=',\n')
  File "<stdin>", line 1
    print(52, sep='!", end=',\n')
                              ^
SyntaxError: unexpected character after line continuation character
 print(52, sep="!", end=',\n')
52,
 print(52, 36, sep="!", end=',\n')
52!36,
 print(52, 36, 45, sep=":", end=',\n')
52:36:45,


