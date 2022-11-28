# Дан CSV файл с данными о товарах (article, title, description, price)
# Необходимо считать файл, привести к списку словарей, выполнить приведение типов значений атрибута price,
# провести валидацию данных с помощью Pydantic, не верные записи вывести в другой файл, а из списка удалить

from pydantic import BaseModel
from csv import DictReader

with open('11.csv', 'r', encoding='utf-8') as file:
    rider = DictReader(file)
    products = list()
    for user in rider:
        products.append(user)  # приведение к списку словарей

    print(products)