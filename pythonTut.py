# Ask the user to input their name and assign it to a variable named name
name = input('What is your name? ')
# Print out hello followed by the name they entered
print('Hello ', name)
# Ask the user to input 2 values
num1, num2 = input('Enter 2 numbers: ').split()
# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)
# Add the values entered
sum = num1 + num2
# Subtract the values
difference = num1 - num2
# Multiply the values
product = num1 * num2
# Divide the values
quotient = num1 / num2
# Use modulus on the values to find remainder
remainder = num1 % num2
# Print results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
