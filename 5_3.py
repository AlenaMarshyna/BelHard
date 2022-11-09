# Вывести четные числа от 2 до n по 5 в строку

while True:
    try:
        n = int(input('Enter n '))
        break
    except ValueError:
        print('It is not a number. Try again')

for i in range(2, n - n%10, 6):
        for j in range(i, i+10, 2):
            print(j, end=' ')
        print()
for k in range(j+2, n, 2):
    print(k, end=' ')
