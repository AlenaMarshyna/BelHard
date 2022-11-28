# Дан файл с текстом, необходимо в проанализировать файл и сказать  сколько слов и букв в каждой строк


with open('10.txt', 'r', encoding='utf-8') as file:
    count_word = 0
    count_let = 0
    for line in file.readlines():
        count_word += len(line.split())
        for word in line.split():
            if word.isalpha():
                count_let += len(word)
    print(count_word, count_let)
