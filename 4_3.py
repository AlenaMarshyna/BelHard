# Заполнить словарь, где ключами будут выступать числа от 0 до n, а значениями вложенный словарь с ключами name email, а
# значения этих ключей будут браться с клавиатуры

n = int(input('Enter n'))

nested_dic = {
    'name': input('Name: '),
    'email': input('email')
}
dictionary = {i: nested_dic for i in range(n+1)}

print(dictionary)
