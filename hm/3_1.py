# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

text = input('Enter your text:\n')

text_new = text.replace(' ', '-')  #1 method

text_in_list = text.split()  #2 method
text_new2 = '-'.join(text_in_list)

#resalt test
print(text_new)
print(text_new2)
