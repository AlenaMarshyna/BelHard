# Дан список чисел, необходимо его развернуть без использования метода revese и функции reversed, а так же дополнительного списка и среза

def revers_num(sp):
    sp = [i for i in sp[::-1]]
    print(sp)

revers_num([1, 2, 3, 4, 5])  # проверка
