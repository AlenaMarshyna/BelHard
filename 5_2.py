# сделать калькулятор, у пользователя спрашивается число, потом действие и второе число
while True:
    try:
        num1 = float(input('Enter fist number: '))
        act = input('Choose +, -, *, / : ')
        num2 = float(input('Enter second number: '))
        break
    except ValueError:
        print('It is not a number. Try again')

if act == '+':
    print(num2+num1)
elif act == '-':
    print(num1-num2)
elif act == '*':
    print(num2*num1)
elif act == '/':
    print(num1/num2)
else:
    print("I can't count it, sorry!")
