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

# class Category(object):
#
#     categories: list[str] = []
#
#     @classmethod
#     def add(cls, category: str) -> int:
#         category = category.title()
#         if category in cls.categories:
#             raise ValueError('category is  not unique')
#         cls.categories.append(category)
#         return cls.categories.index(category)
#         # return len(cls.categories) - 1
#
#     @classmethod
#     def get(cls, pk: int) -> str:
#         try:
#             return cls.categories[pk]
#         except IndexError as e:
#             raise ValueError(e)
#
#     @classmethod
#     def delete(cls, pk: int) -> None:
#         try:
#             del cls.categories[pk]
#         except IndexError:
#             ...  # pass
#
#     # @classmethod
#     # def update(cls, pk: int, new_category_name: str):
#     #     new_category_name = new_category_name.title()
#     #     if new_category_name in cls.categories:
#     #         raise ValueError('category is not unique')
#     #     try:
#     #         cls.get(pk=pk)
#     #     except ValueError:
#     #         cls.add(category=new_category_name)
#     #     else:
#     #         cls.categories[pk] = new_category_name
#
#     @classmethod
#     def update(cls, pk: int, new_category_name: str) -> None:
#         new_category_name = new_category_name.title()
#         if new_category_name in cls.categories:
#             raise ValueError('category is not unique')
#         try:
#             cls.categories[pk] = new_category_name
#         except IndexError:
#             cls.add(category=new_category_name)


class Category(object):

    categories: list[dict] = []

    @classmethod
    def add(cls, category_name: str, is_published: bool) -> int:
        category_name = category_name.title()
        category = tuple(filter(lambda x: x['name'] == category_name, cls.categories))
        if category:
            raise ValueError('category is not unique')
        cls.categories.append(
            {
                'name': category_name,
                'is_published': is_published
            }
        )
        return len(cls.categories) - 1

    @classmethod
    def get(cls, pk: int) -> dict:
        try:
            return cls.categories[pk]
        except IndexError as e:
            raise ValueError(e)

    @classmethod
    def delete(cls, pk: int) -> None:
        try:
            del cls.categories[pk]
        except IndexError:
            ...  # pass

    @classmethod
    def update(cls, new_category_name: str, pk: int) -> None:
        new_category_name = new_category_name.title()
        category = tuple(filter(lambda x: x['name'] == new_category_name, cls.categories))
        if category:
            raise ValueError('category is not unique')
        try:
            cls.categories[pk]['name'] = new_category_name
        except IndexError:
            cls.add(category_name=new_category_name, is_published=False)

    @classmethod
    def make_published(cls, pk: int) -> None:
        try:
            cls.categories[pk]['is_published'] = True
        except IndexError as e:
            raise ValueError(e)

    @classmethod
    def make_unpublished(cls, pk: int) -> None:
        try:
            cls.categories[pk]['is_published'] = False
        except IndexError as e:
            raise ValueError(e)


print(Category.add('Food', True))
print(Category.add('Drink', True))
print(Category.add('food', False))