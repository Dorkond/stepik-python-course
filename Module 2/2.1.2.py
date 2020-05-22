'''
Задание 1
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого
введенного нуля выводит сумму полученных на вход чисел.

Sample input 1:
5
-3
8
4
0
Sample output 1:
14

Sample output 2:
0
Sample output 2:
0
'''

n = int(input())
sum = 0
while n != 0:
    sum += n
    n = int(input())
if n == 0:
    print(sum)