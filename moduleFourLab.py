# Module 5 Lab-5
# Daniel Brooks
# 02/27/25
# Simple function test
# The main function
def main():
# declare local variables
  monthlySales = 0 # monthly sales amount
  storeAmount = 0 # store bonus amount
  empAmount = 0 # employee bonus amount
  salesIncrease = 0 # percent of sales increase
  prompt = "What was your sales this month?"
  promptTwo = 'What was your sale increase this month?"
  getSales(prompt) # call to getSales( )
  getIncrease(promptTwo) # call to getIncrease( )
  calcStoreBonus(monthlySales) # call to calcStoreBonus( )
  calcEmpBonus(salesIncrease) # call to calcEmpBonus( )
  printBonus(storeAmount, empAmount) # call to printBonus
  
# This function gets the monthly sales
def getSales(prompt):
 monthlySales = float(input(prompt))
 return monthlySales

# This function gets the percent of increase in sales
def getIncrease(prompt):
  salesIncrease = float(input(prompt))
  salesIncrease = salesIncrease / 100
  return salesIncrease 
  
# This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
  if monthlySales >= 110000:
    storeAmount = 6000
  elif monthlySales >= 10000:
    storeAmount = 5000
  elif monthlySales >= 90000:
    storeAmount = 4000
  elif monthlySales >= 80000:
    storeAmount = 3000
  else: 
    storeAmount = 0
  return storeAmount

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
  if salesIncrease >= .05:
    empAmount = 75
  elif salesIncrease >= .04:
    empAmount = 50
  elif salesIncrease >= .03:
    empAmount = 40
  else: 
    empAmount = 0
  return empAmount
  
  # This function prints the bonus information
def printBonus(storeAmount, empAmount):
  print("The store bonus amount is $", storeAmount)
  print("The employee bonus amount is $", empAmount)
  if (storeAmount == 6000 ) and (empAmount == empAmount):
    print('Congrats! You have reached the highest bonus amounts possible! ')

# calls main
main()
