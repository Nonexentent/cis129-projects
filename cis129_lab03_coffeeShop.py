'''This is a simple script that has two items for a coffee shop and after taking the order prints out the receipt.'''
stars = "***************************************"
print(stars)
numberOfCoffee = int(input("How much coffee would you like to purchase? Coffe is $5. "))
numberOfMuffins = int(input("How many muffins would you like to purchase? Muffins are $4. "))
numberOfTea = int(input("How many cups of tea would you like to purchase? Tea is $2.50 a cup. "))
numberOfBread = int(input("How many slices of bread would you like to purchase? Bread slices are $1.25 a slice. ")
print(stars)
coffeePrice = 5.0
muffinPrice = 4.0
teaPrice = 2.5
breadPrice = 1.25
tax = 1.06
print('''My Coffee and Muffin Shop
Number of coffees bought?''')
print(numberOfCoffee)
print("Number of muffins bought?")
print(numberOfMuffins)
print(stars)
print("")
total = (((coffeePrice * numberOfCoffee) + (muffinPrice * numberOfMuffins) + (numberOfTea * teaPrice) + (numberOfBread * breadPrice)) * tax)
taxTotal = (total * .06)
print(stars)
print("My Coffee and Muffin Shop Receipt")
print(numberOfCoffee, "Coffee at $5 each: $", (numberOfCoffee * coffeePrice))
print(numberOfMuffins, "Muffins at $4 each: $", (muffinPrice * numberOfMuffins))
print(numberOfTea, "Cups of Tea at $2.50 each: $", (numberOfTea * TeaPrice))
print(numberOfBread, "Bread slices at $1.25 each: $", (breadPrice * numberOfBread))
print("6% tax: $ ", taxTotal)
print("---------")
print("Total: $", total)
print(stars)
print("Thank you for your purchase, please come again!")
