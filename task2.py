# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


my_list = [2, 4, 6, 8, 10]
print(f'Список из пяти элементов\n {my_list}')
a = my_list[::len(my_list)-1]
b = my_list[1::len(my_list)-3]
c = my_list[2:len(my_list)-2] * 2
print(a)
print(b)
print(c)

import math
print((math.prod(a)))
print((math.prod(b)))
print((math.prod(c)))
