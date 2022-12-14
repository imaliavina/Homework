# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_lst = [3, 1, -4, 5, 7, 3, -9, 6, 2]

summa = 0

for i in range(len(my_lst)):
    if i%2 == 1:
        summa += my_lst[i]

print(my_lst)
print(f'Сумма на нечетных позициях: {summa}')

# 23. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_lst1 = [3, 1, -4, 5, 7, 3, -9, 6, 2]
my_lst2 = [2, -1, -4, 8, -2, 5, 9, 4]

def mult_pairs(my_lst):

    new_lst = []
    l = len(my_lst)

    if l%2 == 0:
        m = l//2
    else:
        m = l//2 + 1

    for i in range(m):
        new_lst.append(my_lst[i] * my_lst[l-1-i])

    print(f'Исходный лист: {my_lst}')
    print(f'Лист произведений пар: {new_lst}')

mult_pairs(my_lst1)
mult_pairs(my_lst2)

# 24. Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

my_lst = [3.4, 4.6, 1.15, 2.45, 5, 7.657, -3.1]
max_fl_part = 0
min_fl_part = 1

for i in range(len(my_lst)):
    if my_lst[i] > 0:
        fl_part = my_lst[i] - math.floor(my_lst[i])
    else:
        fl_part = 1 - (my_lst[i] - math.floor(my_lst[i]))   #если чило отрицательное

    if fl_part < min_fl_part:
        min_fl_part = round(fl_part, 2)
    if fl_part > max_fl_part:
        max_fl_part = round(fl_part, 2)


print(f'Минимальная вещ. часть {min_fl_part}')
print(f'Максимальная вещ. часть {max_fl_part}')
print(f'Разница между макс. и мин. дробных частей: {max_fl_part - min_fl_part}')

# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

dex = int(input('Введите число в десятичной форме:'))
b = ''

while dex > 0:
    b += str(dex % 2)
    dex = dex//2

print(int(b))


# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число:'))

f, f_negative = [], []
f.append(0)
f.append(1)
f_negative.append(1)

for i in range(2, n+1):
    f.append(f[i-2] + f[i-1])
    f_negative.append(((-1)**(i+1)) * (f[i-2] + f[i-1]))

print(f_negative[::-1] + f)






