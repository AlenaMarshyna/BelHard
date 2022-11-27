# Реализовать класс Category/ Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать ошибку ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать атрибут ValueError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод update принимающий индекс категорий и новое название категории, если
# нет элемента на таком индексе, то новая категория должна добавляться с учетом того, что
# имена категорий уникальны, если новое имя категории нарушает уникальность в списке
# категорий, вызвать исключение ValueError

class Category:

    def __init__(self, categories: list) -> None:
        self.categories = categories

    def add(self, txt: str) -> int:
        self.txt = txt
        if self.txt in self.categories:
            raise ValueError
        else:
            self.categories.append(txt)
            return self.categories.index(txt)

    def get(self, i: int) -> str:
        self.i = i
        if self.categories[self.i]:
            return self.categories[self.i]
        else:
            raise ValueError

    def delete(self, j) -> None:
        self.j = j
        if j <= len(self.categories):
            del self.categories[self.j]

    def update(self, k: int, name: str) -> None:
        self.k = k
        self.name = name
        if self.name not in self.categories and self.categories[self.k] != self.name:
            return self.categories.append(self.name)
        elif self.name in self.categories:
            raise ValueError


print(Category(['A', 'B', 'C']).add('D'))  # проверка
print(Category(['A', 'B', 'C']).get(1))  # проверка
print(Category(['A', 'B', 'C', 'E']).delete(5))  # проверка
print(Category(['A', 'B', 'C', 'E']).update(3, 'B'))  # проверка
