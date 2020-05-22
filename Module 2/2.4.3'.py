'''
String slicing

dna = 'ATTCGGAGCT'
dna[1] -> T
dna[1:4] -> TTC
dna[:4] -> ATTC
dna[4:] -> GGAGCT
dna[-4:] -> c четвертого символа с конца и до конца -> AGCT
dna[1:-1] -> с первого до последнего символа (но последний символ не берём)
dna[1:-1:2] -> ходим так же как и в предыдущем, но с шагом в 2 -> TCGG
dna[::-1] -> TCGAGGCTTA

Задача - палиндром
Дана геномная последовательность.
Проверить, является ли она палиндромом.
Строка считается палиндромом, если читается в обоих направлениях одинаково
Входные данные:
CAGGTGGAC       GATTACA
YES             NO

s = input()
i = 0
j = len(s)-1
is_palindrom = True
while i < j
    if s[i] != s[j]:
        is_palindrom = False
    i += 1
    j += 1
if is_palindrom:
    print('YES')
else:
    print('NO')

'''
s = 'abcdefghijk'
print(s[-1:-10:-2])
