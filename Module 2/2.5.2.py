'''
Удаление элемента из списка
students = ['Ivan', 'Masha', 'Sasha']
students.remove('Sasha') - удаляет первое вхождение

del students[0] - удаляет первый элемент

Поиск элемента в списке
students = ['Ivan', 'Masha', 'Sasha']
if 'Ivan' in students:
    print('Ivan is here!')
if 'Ann' not in students:
    print('Ann is out')

ind = students.index('Sasha') - 2
ind = students.index('Ann' - ValueError: 'Ann" is not in the list

Сортировка списка
Не изменяя порядка изначального списка
students = ['Sasha', 'Ivan', 'Masha']
ordered_students = sorted(students) - в возрастающем порядке
Результат: ['Ivan', 'Masha', 'Sasha']

Изменяя сам список
students.sort()
min(), max() - возвращают максимальное значение в списке
Для применения всех вышеназыванных методов необходимо, чтобы все элементы списка были сравнимы.

Список в обратном порядке
students = ['Sasha', 'Ivan', 'Masha']
students.reverse() - изменяет список
reversed(students) - не изменяет список
students[::-1]

Присвоение списков
a = [1, 'A', 2]
b = a
a[0] = 42
значение первого элемента в списке b - 42
b[2] = 30
значение последнего элемента в списке a - 30

'''
a = [1, 2, 3]
b = a
# значения списка b?
print(b)

a[1] = 10
# значения списка b?
print(b)

b[0] = 20
# значения списка a?
print(a)

a = [5, 6]
# значения списка b?
print(b)
