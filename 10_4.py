# В файле записано стихотворение. Выведите его на экран, а также
# укажите, каких слов в нем больше: начинающихся на гласную или на согласную букву (без учета регистра)?


with open('text.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():  # вывод стихотворения
        print(line, end='')

with open('text.txt', 'r', encoding='utf-8') as file:
    a = ['а', 'у', 'е', 'о', 'э', 'я', 'и', 'ю', 'ё']
    count1 = 0
    count2 = 0
    for line in file.readlines():
        for word in line.split():
            word = word.lower()
            if word[0] in a:
                count1 += 1
            else:
                count2 += 1
    if count1 > count2:
        print('Больше слов с глассной буквы')
    else:
        print('Больше слов с согласной буквы')
