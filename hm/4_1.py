# Заполнить список степенями числа 2

n = int(input('Enter number for degree: '))
degree_2 = [2 ** i for i in range(1, n+1)]
print(degree_2)
