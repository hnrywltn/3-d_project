person = {'Christopher': {
    'Middlename': 'Niles',
    'Lastname': 'Jack',
    'scores': [64, 46, 67, 98, 59]
}}
# person['last'] = 'Harrison'
# print(person['Christopher']['scores'][0])
# print(person['first'])
sum = 0
for i in range(len(person['Christopher']['scores'])):
    sum += person['Christopher']['scores'][i]
avg = sum / len(person['Christopher']['scores'])
# print(avg)
person['Christopher']['average'] = avg
print(person['Christopher']['average'])