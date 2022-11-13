#Написать функцию перевода десятичного числа в двоичное и обратно, без
 использования функции int


def code(n):
    num = ''
    num_10 = 0
    while n:
        num += str(n % 2)
        n //= 2
    num = num[::-1]
    print('в двоичной системе: ', num)
    for i in range(len(num)):
        if num[i] == '1':
            num_10 += 2**(i+1)
    print('в десятичной: ', num_10)
