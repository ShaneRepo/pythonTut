# Different output based on age
# 1 - 18 -> important
# 21, 50, > 65 -> not important
# All others -> not important
# Receive age
age = eval(input("Enter age: "))
# If both true returns true
# If either condition is true then true
# Convert a true condition into false
# If age is both greater than or equal to 1 and less than or equal to 18 important
if (age >= 1) and (age <= 15):
    print("Important Birthday")
# If age is either 21 or 50 important
elif (age == 21) or (age == 50):
    print("Important Birthday")
# If age is less than 65 convert true to false and vice versa
elif not (age < 65):
    print("Important Birthday")
# Else not important
else:
    print("Sorry Not Important")
