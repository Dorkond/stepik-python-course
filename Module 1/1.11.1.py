# Строки в Python - последовательность символов, не важно каких
# Есть несколько способов записать строку в Python
#   'string1'
#   "string"
#   '''multiple lines
#   string'''               три одинарные кавычки
#   """multiple lines
#   string"""               три двойные кавычки

# Некоторые операции со строками
# 'abc' + 'def' = 'abcdef'         конкатенация(или просто склейка) строк
# 'abc' * 3 = 'abcabcabc'          конкатенация n строк
# len('abcdef') = 6                длина строки

# Сравнение строк
# Строки сравниваются в лексикографическом порядке (как в орфографическом словаре)
# 'abc' == '''abc'''
# 'abc' < 'ac'
# 'abc' > 'ab'

# Символ перевода строки
# '\n' - cимвол перевода строки
# print('First line', '\n\n', 'Last line')
# Результат:
# First line
#
#
# Last line

# Комментарии
x = 5  # комментарий к действию

'''
Многострочный комментарий - это
просто строка
'''