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
        txt = str(input())
        if not txt in self.categories:
            catevories.append(txt)
            return categories.index(txt)
        else:
            raise ValueError
    
    def get(self, i: int) -> str:
        i = int(input())
        if categories[i]:
            return categories[i]
        else:
            raise ValueError
    
    def delete(self, j: int) -> None:
       j = int(input())
       if categories[j]:
           del categories[j]
   
    def update(self, k: int, name: str) -> None:
           k = int(input())
           name = input()
           if not categories[k] and not name in categories:
               categories.append(name)
           elif name in categories:
               raise ValueError
               
               
               
n = Category(['A', 'B', 'C'])
print(Category(['A', 'B', 'C']).add('C'))



