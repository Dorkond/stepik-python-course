'''
Рассмотрим две структуры данных, которые наравне со списками активно используются в Python
Это множества и словари
Множества позволяют хранить некий набор данных и быстро отвечать на запрос присутствия этого
элемента в множестве.

Множество - тип данных set
    s = set() - создание пустого множества
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket) -> {'orange', 'banana', 'pear', 'apple'} -

    порядок произвольный тк это множество
    (порядок не имеет значения)

    'orange' in basket - True
    'python' in basket - False

Операции с множествами
    s.add(element)
    s.remove(element) -> удаляет элемент, если такого элемента нет -> ошибка
    s.discard(element) - не вызывает ошибок
    s.clear() - очисить
    len(s) - количество элементов

Перебор элементов множества

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
for x in basket
    print(x)

banana
apple
orange
pear

Словари позволяют хранить множество пар: ключ - значение и по первому элементу пары получать
соответствующее ему значение. (отличие от листов - идентификатором элемента может на практике
быть не только число)

Словарь(dictionary), отображение(map), ассоциативный массив.

    dict или  {} - инициализация
    d = {'a': 239, 10: 100}
    print(d['a'])
    print(d[10])

Операции со словарями
    key in dictionary
    key not in dictionary       -> True or False
    dictionary[key] = value     -> добавление элемента в словарь
    dictionary[key]             -> выдаст значение соотв key, ошибка если key нет в dict
    dictionary.get(key)         -> не будет ошибки (None)
    del dictionary[key]         -> удаление

Словари:
    Изменяемы                   -> понятно
    Элементы не имеют порядка   -> как во множествах
    Все ключи различны          -> если уже по существующему ключу добавить элем в словарь то он перетрется
    Ключи неизменяемы           -> ключами не могут быть динамические объекты

Перебор элементов словаря
    d = {'C': 14, 'A': 12, 'T': 9, 'G': 18}
    for key in d:
        print(key, end=' ')         -> G C A T
    for key in d.keys():
        print(key, end=' ')         -> G C A T
    for value in d.values():
        print(value, end=' ')       -> 18 14 12 9
    for key, value in d.items():
        print(key, value, end=';')  -> G 18; C 14; A 12; T 9;

Мы можем сопоставлять одному ключу не одно значение, а список значений.
Например - по номеру автомобиля - много владельцев. 




'''