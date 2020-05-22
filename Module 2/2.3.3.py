'''
Рассмотрим ещё одну задачу на цикл for
Вывести сумму всех нечётных чисел от a до b

a,b=input().split()
a = int(a)
b = int(b)
s = 0
for i in range(a,b+1)
    if i % 2 == 1:
        s+=i
print(s)

Немного модифицируем предыдущее решение, будем сразу идти по нечётным числам

a,b=input().split()
a = int(a)
b = int(b)
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b+1, 2)
    s += i
print(s)

Ещё одна модификация этой задачи, на этот раз модифицируем ввод данных
Можно использовать list comprehention

a,b = (int(i) for in input().split())
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b+1, 2)
    s += i
print(s)

'''