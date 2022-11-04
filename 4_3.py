# Заполнить словарь, где ключами будут выступать числа от 0 до n, а значениями вложенный словарь с ключами name email, а
# значения этих ключей будут браться с клавиатуры

n = int(input('Enter n: '))

dictionary = {i: {input('enter name: '): input('enter email: ')} for i in range(n)}

print(dictionary)
