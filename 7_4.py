# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё
# место в строю. Помогите ему это сделать. Программа получает на вход невозрастающую
# последовательность натуральных чисел, означающих рост каждого человека в строю. После
# этого вводится число X – рост Пети. Все числа во входных данных натуральные и не  превышают 200

def place_line(height:list, h: int) -> int:
    height.append(h)
    height.sort(reverse=True)
    print(*height)
    return height.index(h) + 1


print(place_line([195, 190, 190, 182, 182, 180, 165, 160], 187))  #check
