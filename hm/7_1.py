# Написать функцию horse принимающая координаты (два числа в диапазоне от 0 до 8)
# расположения коня на шахматной доске, вывести все позиции куда может перейти конь за 1  шаг

#while True:
    #x, y = int(input('Enter x from 1 to 8: ')), int(input('Enter y from 1 to 8: '))
    #try:
        #if 1 <= x <= 8 and 1 <= y <= 8:
            #break
    #except ValueError:
        #print('Not number. Try again')
    #else:
        #print('Going off the chessboard. Try again')


def horse(x: int, y: int) -> list:
    step = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, -2], [-1, 2], [-2, 1], [-2, -1]]
    position = []
    chess = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in step:
        if x + i[0] in chess and y + i[1] in chess:
            position.append([x + i[0], y + i[1]])
    return position


print(horse(4, 4))  # проверка
