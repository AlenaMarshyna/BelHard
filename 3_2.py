#Пользователь вводит три числа,найти среднее арифметическое с точностью 3

num1, num2, num3 = int(input()), int(input()), int(input())

average = (num1 + num2 + num3)/3

print(round(average, 3))
