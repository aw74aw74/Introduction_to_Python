# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

list_len = int(input("Введите длину списка: "))
number_for_search = int(input("Введите число: "))
list_my = list()
count_number=0
for i in range(list_len):
    list_my.append(randint(0, 10))
    if number_for_search==list_my[i]:
        count_number+=1
print(list_my)
print('Число {} встречается {} раз(а)'.format(number_for_search, count_number))