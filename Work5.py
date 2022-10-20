def scale2for9(n, scale, n_float):
    answer = ''
    while n > 0:
        answer = str(n % scale) + answer
        n = n // scale
    if n_float != 0:
        n_float = float('0.'+str(n_float))
        answer += '.'
        for i in range(4):
            n_float *= scale
            if n_float > 0:
                answer += str(n_float)[0:1]
                n_float -= int(str(n_float)[0:1])

            else:
                answer += '0'
    return answer


s = input('Введите число(если вещественное, то через точку): ')
num_float = 0
if '.' in s:
    num_int, num_float = [int(x) for x in s.split(sep='.')]
else:
    num_int = int(s)
scale1 = int(input('Введите целевую систему счисления(от 2 до 9): '))
if scale1 < 2 or scale1 > 9:
    print('Ошибка. Неправильно введена система счисления.')
    exit()
if num_int < 0:
    num_int = -1*num_int
    print('-'+scale2for9(num_int, scale1, num_float))
else:
    print(scale2for9(num_int, scale1, num_float))
if num_float != 0:
    print('Точность 4 знака')
