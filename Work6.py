from random import random, randint


def array_generation(n):
    s = []
    for i in range(0, n):
        s.append(random() + randint(-100, 100))
    return s


def maximum_search(array):
    maximum = array[0]
    maximum_num = 0
    for i in range(1, len(array)):
        if array[i] > maximum:
            maximum = array[i]
            maximum_num = i
    return maximum_num


def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def array_output(array):
    for i in array:
        print(i, end=' ')
    print()


def nuller(array, number):
    for i in range(number+1, len(array)):
        array[i] = 0
    return array


k = input('Введите размерность массива: ')
if not(is_number(k)):
    print('Ошибка. Неправильный тип переменной.')
    exit()
k = int(k)
if k <= 0:
    print('Ошибка. Неправильное значение переменной.')
    exit()
m = array_generation(k)
array_output(m)
array_output(nuller(m, maximum_search(m)))
