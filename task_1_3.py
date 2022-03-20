i = int(input('Введите количество процентов: '))
for i in range (1, 101):
    if i % 10 == 1 and i != 11:
        print(i , 'процент')
    elif 1 < i % 10 < 5 and not 11 < i % 100 < 15:
        print(i, 'процента')
    else:
        print(i, 'процентов')
