#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
my_list = []

for i in range(5):
    index = random.randint(0, 2)
    my_list.append(round(random.uniform(0,10), index))

a = max(my_list)
b = min(my_list)
f = round(a - int(a), 2)
g = round(b - int(b), 2)
diff = round(abs(f - g), 2)

print('Вот список рандомных чисел\n', my_list)
print ('Max:', max(my_list), 'Min:', min(my_list))
print('Разница дробной части между максимальным и минимальным числами:', diff)

