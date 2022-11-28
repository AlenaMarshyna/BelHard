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
    
    categories: list
    
    @classmethod
    def add(cls, categories: list, name: str) -> int:
        if name in categories:
            raise ValueError
        else:
            categories.append(name)
            return categories.index(name)
    
    @classmethod
    def get(cls, categories: list, i: int) -> str:
        if categories[i]:
            return categories[i]
        else:
            raise ValueError
    
    @classmethod
    def delete(cls, categories: list, i: int) -> None:
        if i <= len(categories):
            del categories[i]
    
    @classmethod
    def update(cls, categories:list,  i: int, name: str) -> None:
        if name not in categories and categories[i] != name:
            return categories.append(name)
        elif name in categories:
            raise ValueError


print(Category().add(['A', 'B', 'C'], 'D'))  # проверка


# Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool)
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение ValueError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение  ValueError

class NewCategory(Category):  # дочерний класс, где меняю атрибут на список словарей и добавляю новые методы

    def __init__(self, categories: list[dict], name: str, is_published: bool) -> None:
        super().__init__(categories)
        self.name = name
        self.is_published = is_published
        self.categories = [{self.name: self.is_published}]
        self.j = None

    def make_published(self, j: int) -> None:
        self.j = j
        if not self.categories[self.j]:
            raise ValueError
        else:
            self.categories[self.j][self.is_published] = True

    def make_unpublished(self, j: int) -> None:
        self.j = j
        if not self.categories[self.j]:
            raise ValueError
        else:
            self.categories[self.j][self.is_published] = False


# проверка
print(NewCategory([{'A': True}, {'B': False}]))
