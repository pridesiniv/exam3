def palindrom():
    word = input('Введите слово для проверки на палиндромность\n')
    drow = word[::-1]
    if word == drow:
        print('Палиндром!!')
    else:
        print('Не палиндром')
palindrom()