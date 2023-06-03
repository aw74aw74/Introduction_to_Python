# ----------Задача---------
# Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
# ----------Решение--------

# string_my = "a a a b c a a d c d d"
# list_my = list(string_my.split(" "))
# set_my = set(list_my)
# for i in set_my:
#     count = 0
#     for j in range(len(list_my)):
#         if i == list_my[j]:
#             if count > 0:
#                 list_my[j] = i + f"_{count}"
#             count += 1
# print(string_my)
# print(" ".join(list_my))


# import random

# list_my = [random.randint(0, 10) for _ in range(20)]
# counter = {}
# print(list_my)
# for item in list_my:
#     counter[item] = counter.get(item, 0) + 1
#     # print(counter)
#     print(
#         item
#         if counter.get(item) < 2
#         else (str(item) + "_" + str(counter.get(item) - 1)),
#         end=" ",
#     )


# ----------Задача---------
# Задача №27.
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
# ----------Решение--------
# from string import punctuation

# my_string = """She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells"""
# for ch in punctuation:
#     my_string = my_string.replace(ch, "")
# print(len(set(my_string.lower().split())))


# ----------Задача---------
# Задача №29.
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 
# ----------Решение--------

# Ваня:
n = int(input())
max_number = 0
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)