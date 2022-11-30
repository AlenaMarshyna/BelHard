# Дан CSV файл с данными о товарах (article, title, description, price)
# Необходимо считать файл, привести к списку словарей,
# выполнить приведение типов значений атрибута price,
# провести валидацию данных с помощью Pydantic,
# неверные записи вывести в другой файл, а из списка удалить

from pydantic import BaseModel, ValidationError
from csv import DictReader, DictWriter

with open('11.csv', 'r', encoding='utf-8') as file:
    rider = DictReader(file)
    products = list()
    for user in rider:
        products.append(user)  # приведение к списку словарей
    for j in products:
        j['price'] = float(j['price'])
    print(products)

    class Config(BaseModel):
        article: str
        title: str
        description: str
        price: float


    # products2 = [Config(**product) for product in products]

    try:
        products2 = [Config(**product) for product in products]
    except ValidationError:
        text = open("11+.csv", "w")
        text.write(products)

    print(products)


