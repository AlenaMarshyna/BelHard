# Написать класс Numbers
# Конструктор класса принимает список чисел numbers: list[int]
# Написать метод average — возвращающий среднее арифметическое между всеми числами
# Написать метод max_count — возвращающий число из списка, которое чаще встречается, 
# если таких чисел несколько, вывести среднее арифметическое среди таких чисел

from collections import Counter

class Numbers:
    
    def __init__(self, numbers: list[int]) -> None:
        self.numbers = numbers
    
    def average(self) -> float:
        return sum(self.numbers) / len(self.numbers)
        
    def max_count(self) -> float:
        my_dict = dict(Counter(self.numbers))
        max_value = max(my_dict.values())
        new_dict = {key1: num for key1, num in my_dict.items() if num == max_value}
        #print(new_dict)

        if len(new_dict) > 1:
            return sum(new_dict) / len(new_dict)
        else:
            return max_value[0]


numbers1 = Numbers([1, 3, 4, 1, 3, 1, 4, 3])

print(numbers1.average())
print(numbers1.max_count())
