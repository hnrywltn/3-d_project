# ask a user to enter their first name and store it in a variable
# ask a user to enter their last name and store it in a variable
# print their full name
# Make sure you have a space between first and last name
# Make sure the first letter of first name and last name is uppercase
# Make sure the rest of the name is lowercase
print("Please enter names using proper grammar")
FN = input('Enter First name')
LN = input('Enter Last name')
print("Good day, " + str(FN.capitalize()) + ' ' + str(LN.capitalize()))