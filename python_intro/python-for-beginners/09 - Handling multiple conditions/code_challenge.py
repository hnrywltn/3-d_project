# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z
FN = input('What is your first name? ')
if FN.lower().startswith('a') or FN.lower().startswith('b'):
    print('Please go to room AB.')
elif FN.lower().startswith('c'):
    print("Please go to room CD.")
else:
    LN = input('What is your last name? ')
    if LN.lower().startswith('z'):
        print('Please go to room Z.')
    else:
        print("Please go to room OTHER.")
# ok.