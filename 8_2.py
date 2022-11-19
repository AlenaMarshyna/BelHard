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
        c = dict(Counter(self.numbers))
        max_value = max(c.values())
        final_dict = {k: v for k, v in c.items() if v == max_value}
        if count == 1:
            return max_c[0]
        else:
            return sum / count


numbers1 = Numbers([1, 3, 4, 1, 3, 1, 4, 3])

print(numbers1.average())
print(numbers1.max_count())
