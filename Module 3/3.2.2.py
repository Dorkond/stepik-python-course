'''
Напишите функцию update_dictionary(d, key, value), которая принимает на
вход словарь dd и два числа: key и value.

Если ключ key есть в словаре dd, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 * key.
Если и ключа 2 * key2∗key нет, то нужно добавить ключ 2 * key
в словарь и сопоставить ему список из переданного элемента [value].

Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.
'''

def update_dictionary(d, key, value):
    dictionary = d
    a = [value]
    if key in dictionary:
        dictionary[key] += a
    if key not in dictionary:
        if (2 * key) in dictionary:
            dictionary[2 * key] += a
        else:
            d[key * 2] = [value]
    return