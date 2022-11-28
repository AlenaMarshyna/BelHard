# 1. Дан многострочный файл txt
# а) разбить файл на N(вводится с клавиатуры) файлов построчно
# б) разбить файл на несколько файлов по N строк


with open('10.txt', 'r', encoding='utf-8') as file:
    file = file.readlines()
    for i in range(int(input())):
        text = open(f'txt 10 {i}', "w")
        text.write(file[i])

with open('10.txt', 'r', encoding='utf-8') as file:
    file = file.readlines()
    for i in range(len(file) // int(input())):
        text = open(f'txt 10', "w")
        text.write(file[i])
