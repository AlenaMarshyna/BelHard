# Пользователь вводит три числа, сказать сколько из них положительные и сколько отрицательные

num1, num2, num3 = input(), input(), input()

txt = str(num1) + str(num2) + str(num3)
count = txt.count('-')

print('Количество отрицательных чисел = ', count)
print('Количество положительных чисел = ', 3 - count)
