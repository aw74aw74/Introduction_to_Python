# Задача 18: Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

list_len = int(input("Введите длину списка: "))
number_for_search = int(input("Введите число: "))
list_my = list()
position_minimum_difference = 0
minimum_difference = float("inf")
for i in range(list_len):
    list_my.append(randint(0, 100))
    if abs(number_for_search - list_my[i]) < minimum_difference:
        minimum_difference = abs(number_for_search - list_my[i])
        position_minimum_difference = i
print(list_my)
print(
    "Число {} ближе всего к числу {} на позиции {}".format(
        number_for_search,
        list_my[position_minimum_difference],
        position_minimum_difference+1,
    )
)
