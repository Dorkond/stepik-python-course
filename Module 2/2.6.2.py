'''
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно).
На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна
отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
'''
n = int(input())
i = 0
l = []
if n == 1:
    print(1)
    exit()
if n == 2:
    print(1, 2)
    exit()
while len(l) < n:
    for k in range(1, n):
        for j in range(k):
            l.append(k)
            if len(l) >= n:
                print(*l)
                exit(0)
# Ну да, костыли