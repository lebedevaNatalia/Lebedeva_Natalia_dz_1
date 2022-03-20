duration = int(input('Введите количество секунд '))
if 0 < duration < 60:
    print (duration // 60, 'сек')
elif 60 < duration < 3600:
    print (duration // 60, 'мин', duration % 60, 'сек')
elif 3600 < duration < 86400:
    print (duration // 3600, 'час', duration // 60, 'мин', duration % 60, 'сек')
