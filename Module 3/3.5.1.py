'''
Модуль содержит определенные функции и данные в определенном файле.
Объекты из модуля можно импортировать в другие модули.
Имя файла = имя модуля + .py

Импорт модуля
Рассмотрим файл my_module.py
Пусть в нем описана функция foo()

import my_module
my_module.foo()

from my_module import foo
foo()

from my module import *
foo()

from my_module import foo as my_foo
my_foo()

Python распространяется с библиотекой стандартных модулей.
https://docs.python.org/3/library/

Аргументы командной строки
модуль sys
sys.argv - список аргументов командной строки
import sys
print(len(sys.argv))

Запуск внешних процессов
Модуль subprocess
subprocess.call(args, *, stdin = None, stdout = None)
Запускает программу в соответствии с аргументами (args). Дожидается выполнения и возвращает код
возврата.
Например,
subprocess.call(['python', '-h'])

'''