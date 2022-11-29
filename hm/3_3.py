# Пользователь вводит имя, возраст, город, сформировать приветственное сообщение путем форматирования 3-мя способами

name, age, city = input(), int(input()), input()

print('Hello %s. You are %d years old. You are from %s.' % (name, age, city))  # first method
print('Hello {name}. You are {age} years old. You are from {city}.'.format(name=name, age=age, city=city))  # second
print(f'Hello {name}. You are {age} years old. You are from {city}.')  # third method
