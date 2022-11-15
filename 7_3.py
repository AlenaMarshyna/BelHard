# Написать функцию pow, которая принимает число А и число Б, необходимо с помощью
# рекурсии возвести число А в степень Б

while True:
    try:
        a, b = float(input('Enter A: ')), float(input('Enter B: '))
        break
    except ValueError:
        print('Not number. Try again')

def pow(a:float) -> float:
    global b
    if b == 1:
        return a
    else:
        b -= 1
        return a*pow(a)


print(pow(a))
