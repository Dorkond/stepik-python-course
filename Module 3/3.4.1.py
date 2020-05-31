'''
Чтение из файла
    inf = open('file.txt', 'r')
Файл теперь связан с этой переменной. Используя её, можно читать файл построчно.
    s1 = inf.readline()
    s2 = inf.readline()
    inf.close()

Конструкция, которая сама закрывает файл:
    with open('text.txt') as inf:
        s1 = inf.readline()
        s2 = inf.readline()

    Здесь файл уже закрыт

Про путь подробнее тут https://fooobar.com/questions/52653/unicode-error-unicodeescape-codec-cant-decode-bytes-cannot-open-text-files-in-python-3

Пара полезных функций
    s = inf.readline().strip()          -> убирает служебные символы
    '\t abc  \n'.strip() -> 'abc'

    os.path.join('.', 'dirname', 'filename.txt') -> './dirname/filename.txt'
    для того чтобы воспользоваться этой функцией надо подключить модуль os

Построчное чтение файла
with open('input.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)

Запись в файл
    ouf = open('file.txt', 'w')
    ouf.write('Some text\n')
    ouf.write(str(25))
    ouf.close()

    with open('text.txt', 'w') as ouf:
        ouf.write('Some text\n')
        ouf.write(str(25))

    Здесь файл уже закрыт
'''