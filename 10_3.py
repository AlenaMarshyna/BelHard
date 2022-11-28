# 1. Дан многострочный файл txt
# а) разбить файл на N(вводится с клавиатуры) файлов построчно
# б) разбить файл на несколько файлов по N строк


with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(int(input())):
        file.write(lines[i])
