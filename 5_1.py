def nums(num):
    for num in range(1, num + 1, 2):
        yield num


print(*(nums(int(input('Введите число: ')))))
