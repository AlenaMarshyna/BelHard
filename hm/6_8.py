#Дан словарь, ключ - Название страны, значение - список городов, на вход
 поступает город, необходимо сказать из какой он страны

def look_key(dictionery, value):
    for k, v in dictionery.items():
        for i in v:
            if i == value:
                print(k)

d ={
        'Italy': ['Vien', 'Rome', 'some'],
        'Germany': ['Bern', 'Berlin', 'some']
        }

look_key(d, 'Rome')  # проверка
