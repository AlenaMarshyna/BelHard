# Вывести четные числа от 2 до n по 5 в строку

while True:
    try:
        n = int(input('Enter n '))
        break
    except ValueError:
        print('Something wrong. Try again!')

list1 = [str(i) for i in range(2, n, 2)]
for i in range(0, len(list1), 6):
    list1.insert(i+5, '\n')

print(' '.join(list1))
