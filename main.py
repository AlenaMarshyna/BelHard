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
#
#
# from random import triangular
#
# print(triangular(low=1, high=10, mode=1))
#
# from datetime import datetime, timedelta
#
# data = datetime(
#     year=2022,
#     month=12,
#     day=2
# )
#
# data2 = datetime.now()
# print(data)
# print(data2)
# print(data2 - data)
#
# print(data.strftime('%d %B %y %H:%M'))
# data3 = '02 December 22 00:00'
#
# print(datetime.strptime(data3, '%d %B %y %H:%M'))
# delta = timedelta(days=5, hours=3)
# print(data + delta)
#
# from enum import Enum
#
# new*
# class Roles(int, Enum):
#     Admin = 1,
#     User = 3
#
# new*

# from pydantic import BaseModel
#
#
# class Product(BaseModel):
#     article: str
#     title: str
#     description: str = ''
#     price: float
#
#
# with open('products.csv', 'r', encoding='utf-8') as file:
#     headers = file.readline().strip().split(',')
#     products = []
#     invalid_product = []
#     for product in file:
#         values = product.strip().split(',')
#         product = dict(list(zip(headers, values)))
#         if not product['article']:
#             invalid_product.append(product)
#             continue
#         try:
#             product['price'] = float(product['price'])
#         except ValueError:
#             invalid_product.append(product)
#             continue
#         products.append(product)
# with open('invalid_product.csv', 'w', encoding='utf-8') as file:
#     headers = ','.join(headers)
#     for product in invalid_product:
#         values = ','.join(list(product.values()))
#         headers += f'\n{values}'
#     file.write(headers)
#
# products = list(map(lambda x: Product(**x), products))
# print(products)

# import sqlite3
#
# conn = sqlite3.connect('db.sqlite3')
# cur = conn.cursor()
#
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS categories(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(24) NOT NULL UNIQUE,
#         is_published BOOLEAN DEFAULT(false)
#     );
# ''')
# conn.commit()
#
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS products(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(24) NOT NULL,
#         descr VARCHAR(1024),
#         price DECIMAL(7, 2) NOT NULL DEFAULT(0.0),
#         category_id INTEGER NOT NULL,
#         FOREIGN KEY (category_id) REFERENCES categories(id)
#     );
# ''')
# conn.commit()
#
# cur.execute('''
#
# ''')
import asyncio

async def foo():
    for i in range(10):
        print(i)

if __name__ == '__main__':
    asyncio.run((foo()))

import asyncio


async def foo():
    for i in range(10):
        await asyncio.sleep(1)
        print(i)


async def bar():
    for i in 'qwertyuiop':
        await asyncio.sleep(1)
        print(i)


async def main():
    tasks = [asyncio.create_task(foo()) for _ in range(100)]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())


# класс Продукт(БазоваяМодель):
# статья: ул.
# название: ул.
# описание: ул = ''
# цена: плавающая
#
#
# с файлом open('products.csv', 'r', encoding='utf-8'):
# заголовки = file.readline().strip().split(',')
# продуктов = []
# неверный_продукт = []
# для продукта в файле:
# значения = product.strip().split(',')
# product = dict(list(zip(заголовки, значения)))
# если не продукт['статья']:
#invalid_product.append(продукт)
# Продолжить
# пытаться:
# продукт['цена'] = float(продукт['цена'])
# кроме ValueError:
#invalid_product.append(продукт)
# Продолжить
# products.append(продукт)
# с файлом open('invalid_product.csv', 'w', encoding='utf-8'):
# заголовки = ','.join(заголовки)
# для продукта в invalid_product:
# значения = ','.join(list(product.values()))
# заголовки += f'\n{значения}'
# file.write(заголовки)
#
# products = list(map(lambda x: Product(**x), products))
# печать (продукты)
# из моделей импортировать пользователя
#
#
# def send_email(пользователь: Пользователь):
# print(f'сообщение отправлено на {user.email}')
#
#
# пользователи = User.all()
# для пользователя в пользователях:
# send_email(пользователь=пользователь)
    
