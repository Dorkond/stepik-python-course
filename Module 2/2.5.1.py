'''
Списки широко используются для хранения наборов значений и для их дальнейшей манипуляции.
Элементами списка могут быть произвольные значения строки, числа, даже сами списки.
В рамках одного списка можно комбинировать объекты разных типов.

students = ['Ivan', 'Masha', 'Sasha']
for student in students:
    print("Hello, " + student + "!")

Hello, Ivan!
Hello, Masha!
Hello, Sasha!

К каждому элементу списка можно получить доступ с помощью индексов
students = ['Ivan', 'Masha', 'Sasha']
Длина списка: len(students) -> 3

students[0] - 'Ivan'        students[-1] - 'Sasha'
students[1] - 'Masha'       students[-2] - 'Masha'
Students[2] - 'Sasha'       students[-3] - 'Ivan'

Операции со списками
+
students = ['Ivan', 'Masha', 'Sasha']
teachers = ['Oleg', 'Alex']
students + teachers = ['Ivan', 'Masha', 'Sasha', 'Oleg', 'Alex']

*
[0,1] * 4 = [0, 1, 0, 1, 0, 1, 0, 1]

В отличие от изученных типов данных (int, float, str) - списки(list) являются измняемыми.
Можно изменить конкретный элемент списка
students = ['Ivan', 'Masha', 'Sasha']
students[1] = 'Oleg'
print(students)
['Ivan', 'Oleg', 'Sasha']

Добавление элементов в список
students = ['Ivan', 'Masha', 'Sasha']
students.append('Olga')
students += ['Olga']
students += ['Boris', 'Sergey']
пустой список: students = []

Вставка элементов в список
students = ['Ivan', 'Masha', 'Sasha']
students.insert(1, 'Olga')
['Ivan', 'Olga', 'Masha', 'Sasha']
'''
students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(students)
# ['Ivan', 'Masha', 'Sasha', 'Olga', 'O', 'l', 'g', 'a']

