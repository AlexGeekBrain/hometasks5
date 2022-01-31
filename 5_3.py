from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = (i for i in zip_longest(tutors, klasses))

print(*islice(result, 8))
print(list(islice(result, 1)))
print(type(result))
