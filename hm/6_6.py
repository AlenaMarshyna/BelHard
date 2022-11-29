# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

def sort(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2:
            numbers.append(numbers.pop(i))
            
    print(numbers)

sort([3, 6, 8, 5, 10])  # проверка
