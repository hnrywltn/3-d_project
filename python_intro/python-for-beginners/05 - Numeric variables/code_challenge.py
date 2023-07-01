# Ask a user to enter a number
# Ask a user to enter a second number
# Calculate the total of the two numbers added together
# Print 'first number + second number = answer' 
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10
FN = input('Put in the first number of additive question:')
print(FN + ' ' + 'has been inputted.')
SN = input('Put in the second number of additive question:')
print(SN + ' ' + 'has been inputted.')
print('calculating, please wait..')
print(str(FN) + ' ' + '+' + ' ' + str(SN) + ' ' + '=' + ' ' + str(int(FN) + int(SN)))
# how does error?