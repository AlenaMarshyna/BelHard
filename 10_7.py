# Шифр Вернама
# функция ord возвращает номер символа согласно таблицы кодировки
# функция bin дает бинарное представление десятичного числа в двоичном
# Задача: Даны два файла с текстом одинаковой длинны, первый файл -  сообщение которое необходимо закодировать,
# второй файл - ключ  кодирования/ Необходимо закодировать сообщение с помощью шифра Вернама
# Пример: сообщение: LONDON ключ: SYSTEM В бинарном:
# сообщение: 1001100 1001111 1001110 1000100 1001111 1001110
# ключ: 1010011 1011001 1010011 1010100 1000101 1001101
# ответ: 00011111 00010110 00011101 00010000 00001010 00000011
# Принцип шифра, необходимо сравнить каждый бит, если биты  совпали, то на выходе получаем 0, если не совпали - 1
list1 = []
list2 = []
with open('Vernam1.txt', 'r', encoding='utf-8') as file1, open('Vernam2.txt', 'r', encoding='utf-8') as file2:
    file1.read()
    file2.read()
    # for line in file1.readlines():
    #     for i in line:
    #         numb = ord(i)
    #         list1.append(numb)
    #     print(list1)
