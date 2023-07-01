from array import array
# scores = array('d')
# scores.append(97)
# scores.append(98)
# print(scores)


#         0    1   2   3   4   5   6   7   8   9
scores = [100, 50, 60, 88, 70, 95, 90, 63, 45, 10]



students = {
    'Roman': {
        'CS': 95,
        'English': 100,
        'Tech': 80,
        'Social Studies': 100
    },
    'Henry': {
        'CS': 75,
        'English': 100,
        'Tech': 80,
        'Social Studies': 100
    }
}



# print(scores[2])
print(students['Henry']['Tech'])

# sum = 0

# lengthOfArray = len(scores)

# for i in range(lengthOfArray):
#     sum += scores[i]


# print(sum)
# print('the average of the class scores is: ' + str(sum / len(scores)))
