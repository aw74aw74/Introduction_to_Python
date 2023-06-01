# ----------Задача---------
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# ----------Решение--------
# from random import randint

# length = int(input("Введите длину списка: "))
# list_1 = list()
# for i in range(length):
#     list_1.append(randint(0, 100))
# list_1 = set(list_1)
# print(list_1)
# print("Количество различных чисел: ", len(list_1))


# ----------Задача---------
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность на K элементов вправо.
# ----------Решение--------
# from random import randint

# list_len = int(input("Введите длину списка: "))
# offset_k = int(input("Введите смещение: "))
# list_my = list()
# for i in range(list_len):
#     list_my.append(randint(0, 100))
# print(list_my)
# for i in range(offset_k):
#     list_my.insert(0, list_my.pop())
# print(list_my)


# ----------Задача---------
# Напишите программу для печати всех уникальных значений в словаре.
# ----------Решение--------
# my_dict = {
#     "IV": "S001",
#     "V": "S002",
#     "VI": "S001",
#     "VII": "S005",
#     "VIII": "S005",
#     "IX": "S009",
#     "X": "S007",
# }
# print(set(list(my_dict.values())))

# my_dict = [
#     {"IV": "S001"},
#     {"V": "S002"},
#     {"VI": "S001"},
#     {"VII": "S005"},
#     {"VIII": "S005"},
#     {"IX": "S009"},
#     {"X": "S007"},
# ]
# my_list = list()
# for i in range(len(my_dict)):
#     # my_list.append(my_dict[i].values())
#     my_list += my_dict[i].values()
# print(set(my_list))

# my_dict = [
#     {"IV": "S001"},
#     {"V": "S002"},
#     {"VI": "S001"},
#     {"VII": "S005"},
#     {"VIII": "S005"},
#     {"IX": "S009"},
#     {"X": "S007"},
# ]
# my_list = list()
# for item in my_dict:
#     for values in item.values():
#         my_list.append(values)
# print(set(my_list))


# ----------Задача---------
# Дан список, состоящий из целых чисел. напишите программу,
# которая подсчитает количество элементов списка,
# больших предыдущего.
# ----------Решение--------
# from random import randint

# list_len = int(input("Введите длину списка: "))
# list_my = list()
# for i in range(list_len):
#     list_my.append(randint(0, 10))
# count_my = 0
# for i in range(1, list_len):
#     if list_my[i] > list_my[i - 1]:
#         count_my += 1
# print(list_my)
# print(count_my)
