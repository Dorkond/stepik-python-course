'''
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень
пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке.
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].

Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a≤b, c≤d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков —
заголовочные столбец и строка таблицы.
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('\t',end='')
for k in range(c,d+1,1):
    print(k, end='\t')
print()
for i in range(a,b+1,1):
    print(i,end='\t')
    for j in range(c,d+1,1):
        print(i*j,end='\t')
    print()



