# Вывести четные числа от 2 до n по 5 в строку

while True:
    try:
        n = int(input('Enter n '))
        break
    except ValueError:
        print('It is not a number. Try again')

for i in range(2, n - n % 10, 10):
    for j in range(5):
        print(i, end=' ')
        i += 2
    print()

for i in range(n - n % 10 + 2, n, 2):
    print(i, end=' ')
