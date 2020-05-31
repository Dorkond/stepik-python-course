'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''

import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
sample = 'https://stepic.org/media/attachments/course67/3.6.3/'
print(r.text)
req = r.text
seq = r.text[0:2:]
while seq != 'We':
    req = requests.get(sample + req)
    req = req.text
    print(req)
    seq = req[0:2:]

# Хорошая пасхалка на Queen :)
