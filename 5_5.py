src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([i for i in src if src.count(i) == 1])

# оптимизация

my_dict = {i: 0 for i in src}

for i in src:
    my_dict[i] += 1

print([i for i in my_dict if my_dict[i] == 1])

# _______________________________

from collections import Counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
num = Counter(src)

numbers = [i for i, n in num.items() if n == 1]
print(numbers)
