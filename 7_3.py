# Написать функцию pow, которая принимает число А и число Б, необходимо с помощью
# рекурсии возвести число А в степень Б


def pow(a:float, b:float) -> float:
    
    if b == 1:
        return a
    else:
        b -= 1
        return a*pow(a, b)


print(pow(2, 4))  # проверка
