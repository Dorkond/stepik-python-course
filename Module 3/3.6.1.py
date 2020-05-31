'''
Установка дополнительных модулей
Для установки библиотек используют conda и pip
conda install requests

Для того чтобы понять, какие функции можно использовать - надо смотреть документацию.

import requests
r = requests.get('http://example.com') - простой GET запрос
print(r.text) - вывод ответа от сервера

import requests
r = requests.get('http://mail.ru')
print(r.text)

url = 'http://mail.ru'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par) передача параметров в запрос
print(r.url) сформированный URL-адрес с учетом параметров GET запроса

url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies) - отправка сформированных cookies на сервер
print(r.text)

print(r.cookies['example_cookie_name']) использование cookies, полученных от сервера

'''
import requests
url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)
print(r.text)

print(r.cookies['http://httpbin.org/cookies'])