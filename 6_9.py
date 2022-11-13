# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа - пустая строка

def get_key(dictionery):
    for key, keys in dictionery.items():
      #  for k in keys.get():
        if keys.get('email') == '' or keys.get('email') == None:
            print(keys.get('name'))

# проверка
d ={
        '111' : {
                    'name' : 'Alena',
                    'last_name' : 'And',
                    'phone' : '12345',
                    'email' : '+375-33-55555'
                    },
        '112' : {
                    'name' : 'Kate',
                    'last_name' : 'Ded',
                    'phone' : '1234567',
                    'email' : ''
                    },
        '113' : {
                    'name' : 'Pit',
                    'last_name' : 'Sam',
                    'phone' : '7778',
                    },
        }

get_key(d)

