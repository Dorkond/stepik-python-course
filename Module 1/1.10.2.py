# Задача
# Даны два числа, надо вывести результат деления первого числа на второе,
# либо вывести сообщение о том, что деление невозможно.

a = int(input())
b = int(input())
if b != 0:
    print(a / b)
else:
    print('Деление невозможно')
    b = int(input('Введите ненулевое значение'))
    if b == 0:
        print('Вы не справились')
    else:
        print(a / b)