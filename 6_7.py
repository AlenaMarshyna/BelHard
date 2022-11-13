# Дан список чисел, необходимо для каждого элемента посчитать сумму его
соседей, для крайних чисел одним из соседей является число с противоположной
 стороны списка


def sum_neighbors(list1):
    list1.append(list1[0])
    list1.insert(p0, list1[-2])
    for i in range(1, len(list1)-1):
        print(int(list1[i-1])+ int(list1[i+1]))

sum_neighbors([1, 2, 3])  # проверка
