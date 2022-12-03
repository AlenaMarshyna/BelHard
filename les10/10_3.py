# 1. Дан многострочный файл txt
# а) разбить файл на N(вводится с клавиатуры) файлов построчно
# б) разбить файл на несколько файлов по N строк

from itertools import zip_longest


n = int(input())
with open('10.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file if line.strip()]
    count = len(lines)// n
    lines_iter = iter(lines)
    lines = list(zip_longest(*([lines_iter]*count)))

for i in range(len(lines)):
    with open(f'{i}.txt', 'w') as file:
        file.write(file[i])

with open('10.txt', 'r', encoding='utf-8') as file:
    file = file.readlines()
    for i in range(len(file) // int(input())):
        text = open(f'txt 10', "w")
        text.write(file[i])
