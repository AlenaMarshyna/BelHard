# Имеются монеты номиналом 1/5/10/25 копеек, написать функцию witcher, принимающая
# сумму в копейках, необходимо рассчитать сколько минимальное количество монет
# номиналом 1/5/10/25 необходимо чтобы составить данную сумму. Прим. 66 = 25 + 25 + 10 + 5 + 1 ответ 5 монет

while True:
    try:
        sum = int(input('Enter sum: '))
        break
    except ValueError:
        print('Not sum')


def witcher(sum: int) -> int:
    count_1 = 0
    count_5 = 0
    count_10 = 0
    count_25 = 0
    count_25 = sum // 25
    # print(count_25)
    count_10 = (sum % 25) // 10
    # print(count_10)
    count_5 = (sum % 25 % 10) // 5
    # print(count_5)
    count_1 = sum % 25 % 10 % 5
    # print(count_1)
    return count_25 + count_10 + count_5 + count_1


print(witcher(sum))
