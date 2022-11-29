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
    
    categories: list[str] = []
    
    @classmethod
    def add(cls, categories: list, name: str) -> int:
        if name in cls.categories:
            raise ValueError
        cls.categories.append(name)
        return cls.categories.index(name)
    
    @classmethod
    def get(cls, i: int) -> str:
        try:
            return cls.categories[i]
        except IndexError as e:
            raise ValueError(e)
    
    @classmethod
    def delete(cls, i: int) -> None:
        try:
            return cls.categories[i]
        except IndexError:
            ...
    
    # @classmethod
    # def update(cls, i: int, name: str) -> None:
    #     if name not in cls.categories and cls.categories[i] != name:
    #         return cls.categories.append(name)
    #     elif name in cls.categories:
    #         raise ValueError


print(Category().add(['A', 'B', 'C'], 'D'))  # проверка


# Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool)
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение ValueError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение  ValueError

class Category:

    categories: list[dict] = []

    @classmethod
    def add(cls, is_published: bool, name: str) -> int:
        category = tuple(filter(lambda x: x['name'] == name, cls.categories))
        if category:
            raise ValueError
        cls.categories.append(
            {
                'name': name,
                'is_published': is_published
            }
        )
        return len(cls.categories) - 1

    @classmethod
    def get(cls, i: int) -> str:
        try:
            return cls.categories[i]
        except IndexError as e:
            raise ValueError(e)

    @classmethod
    def delete(cls, i: int) -> None:
        try:
            return cls.categories[i]
        except IndexError:
            ...


    @classmethod
    def make_published(cls, j: int) -> None:
        try:
            cls.categories[j]['is_published'] = True
        except IndexError as e:
            raise ValueError(e)


    @classmethod
    def make_unpublished(cls, j: int) -> None:
        try:
            cls.categories[j]['is_published'] = False
        except IndexError as e:
            raise ValueError(e)


# проверка
print(Category.make_unpublished([{'name': 'A', 'is_published': True}, {'name': 'B', 'is_published': False}], 1))
