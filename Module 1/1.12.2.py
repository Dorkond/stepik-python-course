'''
Задача 2
Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал
 (−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).
'''
num = int(input())
if -15 < num <= 12 or 14 < num < 17:
    print('True')
elif num >= 19:
    print('True')
else:
    print('False')