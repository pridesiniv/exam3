import time
def carta():
    num = int(input('Введите номер карты'))
    x = str(num)
    if len(x) != 16:
        print('Должно быть 16 цифр, проверьте правильность ввода')
    else:
        print('Обработка. Ожидайте')
        time.sleep(3)
        list_num = list(x)

        encrypted_num = []
        for i, j in enumerate(list_num):
            if i < 12:
                j = '*'
                encrypted_num.append(j)
            else:
                encrypted_num.append(j)
        print(' '.join(encrypted_num))

carta()