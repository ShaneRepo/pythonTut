# Have user enter their investment amount and expected interest
# Each year their investment will increase by their investment + their investment * interest
# Print out the earnings after 10 year period
# Ask for the money invested + interest rate
money = input("How much to invest :")
interest_rate = input("Interest rate :")
# Convert the value to a float
money = float(money)
# Convert value to a float & round percentage rate by 2 digits
interest_rate = float(interest_rate) * .01
# Cycle through 10 years using a for loop and range from 0-9
for i in range(10):
    money = money + (money * interest_rate)
# Output the results
print("Investment after 10 years : {:.2f}".format(money))
