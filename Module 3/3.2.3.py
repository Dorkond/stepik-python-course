'''
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве
используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова,
разделённые пробелом и вывести получившуюся статистику.

Программа должна считывать одну строку со стандартного ввода и выводить для каждого
уникального слова в этой строке число его повторений (без учёта регистра) в формате
"слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно
выводиться только один раз.

a aa abC aa ac abc bcd a

ac 1
a 2
abc 2
bcd 1
aa 2
'''
d = {}
a = [str(i).lower() for i in input().split()]
for x in range(len(a)):
    if a[x] not in d:
        d[a[x]] = 1
    else:
        d[a[x]] += 1
for key, value in d.items():
    print(key, value, end='\n')

