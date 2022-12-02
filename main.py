# def do_something(a, b=6, c=None):
#     if not c:
#         print(a*b)
#     else:
#         print(a+b+c)
#
# a = 5
# b = 10
# do_something(2, 6, 7)
#
# def baz(**kwargs):
#     print(kwargs)
#
# baz(a=1, c=2, i=3)
#
# def do_it(a, b):
#     if a > b:
#         return a+b
#     else:
#         return a*b
# res = do_it(4, 5)
# print(res)
#
# def is_pol(text):
#     return text.lower() == text[::-1].lower()
#
#
# print(is_pol('Holloh'))
#
# def zam(a):
#     def zamok(b):
#         return a*b
#     return zamok
#
# c = zam(4)
# d = zam(8) b
# print(c(5))
# print(d(5))

# def decimal_(dec):
#     bin = ''
#     while dec > 0:
#         bin = str(dec % 2) + bin
#         dec //= 2
#     return bin
#
# print(decimal_(18))

# morse = {
#     'a':'111'
# }
# def text_morse(text):
#     global morse
#     result = ''
#     text = text.lower()
#     for i in text:
#         if i in morse:
#             result += morse[i] + ' '
#         if i == '  ':
#             result += '  '
#     return result

# def list_olffset(lst, n):
#     n -= len(lst) * (n // len(lst))  # dвыкидываем целое цисло цилов
#     lst = lst[-n:] + lst[:-n]
#     return lst
#
# print(list_olffset([1, 2, 3, 4, 5, 6, 7], 13))
#
# lst = [1, 2, True, 'rrr']
# lst = list(filter(lambda x: isinstance(x, str), lst))
# print(lst)
#
# a: int = int(input())
# a += 1
#
# lst = [1, 2, True, 'rrr']
# lst = list(filter(lambda x: isinstance(x, str), lst))
# print(lst)

# file = open('10.txt', 'a', encoding='utf-8')
# text = [int(line.strip()) for line in file if line.strip().isdigit()]
#
#
#
# number = [4, 5, 8]
# text = '\n'.join(list(map(str, number)))
# file.write(text + '\n')
# file.close()

# with open('10.txt', 'r') as file:
#     lines = [line.strip() for line in file if line.strip()]
#     file.seek(0)
#     print(file.read())
#     file.seek(10)
#     print(file.read())

# print(lines)

# import json
#
# with open('new.json', 'r') as file:
#     data = json.load(file)
# print(data)
#
# from pydantic import BaseModel, EmailStr, Field
#
#
# class User(BaseModel):
#     name: str
#     age: int=Field(ge=18, le=60)
#     email: EmailStr
#
# data = {
#     'name': 'vas',
#     'age': 45,
#     'email': '333@mail.ru'
#
# }
#
# vasa = User(**data)
#
# from csv import DictReader, DictWriter
#
# with open('11.csv', 'r') as file:
#     rider = DictReader(file)
#     for us in rider:
#         print(us)

# from mypackage import *
#
# from pandas import DataFrame as df
#
# frame = df(
#     {
#         'name': ['aa', 'bb'],
#         'age': [14, 18]
#     }
# )
#
# try:
#     for line in frame.loc:
#         print(line['name'])
# except KeyError:
#     pass
#
# print(frame[frame['age'] > 14])


from random import triangular

print(triangular(low=1, high=10, mode=1))

from datetime import datetime, timedelta

data = datetime(
    year=2022,
    month=12,
    day=2
)

data2 = datetime.now()
print(data)
print(data2)
print(data2 - data)

print(data.strftime('%d %B %y %H:%M'))
data3 = '02 December 22 00:00'

print(datetime.strptime(data3, '%d %B %y %H:%M'))
delta = timedelta(days=5, hours=3)
print(data + delta)

from enum import Enum

new*
class Roles(int, Enum):
    Admin = 1,
    User = 3

new*

