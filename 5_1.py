# Вычислить первые N целых чисел кратные M и больше K

n, m, k = int(input('Enter n ')), int(input('Enter m ')), int(input('Enter k '))

count = 0
while count < n:
    if k % m:
        k += 1
    else:
        print(k, end=' ')
        k += 1
        count += 1
