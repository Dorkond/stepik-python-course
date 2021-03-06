# В программах всегда происходят какие-либо манипуляции с данными
# Эти данные в python всегда являются объектами
# Каждый объект в python имеет свой тип - фактически задаёт множество значений объекта и операции на нём

# Некоторые стандартные типы
# целые числа - int
# вещественные(с плавающей точкой) - float
# логические - bool
# строковые - str
# Все перечисленные типы являются неизменяемыми

# Тип объекта можно изменить путём преобразования типов
# int(x) - преобразование к целому числу
# float(x) - преобразование к числу с плавающей точкой

# Задание 1
# Приведите к целому типу число 2.99
print(int(2.99))
# Ответ - 2
# int(a) не изменяет саму переменную, а лишь возвращает временную переменную типа int

# Задание 2
# Приведите к целому типу число -1.6
print(int(-1.6))
# Ответ -1

# Задание 3
# Вычислите в python значение выражения
# 9**19 - int(float(9**19))
print(9**19 - int(float(9**19)))
# Ответ - 89
# Заметьте, что используется одно и то же число, но результат получается не нулевой.
# Это показывает различие хранения большого числа в целочисленном типе и типе с плавающей точкой.
# Почему так происходит, можно узнать, прочитав о представлении вещественных чисел в компьютере.
# Можно поискать в интернете различные статьи, вот одна из них: https://habrahabr.ru/post/112953/

# Тип произвольного объекта в python можно узнать с помощью функции type
print(type(7))  # <class 'int'>
print(type(7.0)) # <class 'float'>

