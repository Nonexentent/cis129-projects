'''This is a simple script that has two items for a coffee shop and after taking the order prints out the receipt.'''
stars = "***************************************"
print(stars)
numberOfCoffee = int(input("How much coffee would you like to purchase? Coffe is $5. "))
numberOfMuffins = int(input("How many muffins would you like to purchase? Muffins are $4. "))
print(stars)
coffeePrice = 5
muffinPrice = 4
tax = 1.06
print('''My Coffee and Muffin Shop
Number of coffees bought?''')
print(numberOfCoffee)
print("Number of muffins bought?")
print(numberOfMuffins)
print(stars)
print("")
total = (((coffeePrice * numberOfCoffee) + (muffinPrice * numberOfMuffins)) * tax)
taxTotal = (total * .06)
print(stars)
print("My Coffee and Muffin Shop Receipt")
print(numberOfCoffee, "Coffee at $5 each: $", (numberOfCoffee * coffeePrice))
print(numberOfMuffins, "Muffins at $4 each: $", (muffinPrice * numberOfMuffins))
print(f"6% tax: $ ", taxTotal)
print("---------")
print("Total: $", total)
print(stars)
