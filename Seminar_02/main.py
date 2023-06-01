# ----------Задача---------
# Факториал
# ----------Решение--------

# number = int(input("Введите число: "))
# factorial = 1
# for i in range(1, number):
#     factorial *= i + 1
# print(factorial)

# ----------Задача---------
# Фибоначчи
# ----------Решение--------
# number = int(input("Введите число: "))
# fibon1 = 1
# fibon2 = 1
# i = 2
# while number > fibon1:
#     fibon1, fibon2 = fibon1 + fibon2, fibon1
#     i += 1
# if number == fibon1:
#     print(i)
# else:
#     print(-1)

# ----------Задача---------
# Арбузы
# ----------Решение--------
# from random import randint

# count = int(input("Введите количество арбузов: "))
# i = 0
# min_count = 0
# min_weight = float("inf")
# max_count = 0
# max_weight = float("-inf")
# while i < count:
#     i += 1
#     current = randint(1, 30000)
#     if min_weight > current:
#         min_count = i
#         min_weight = current
#     if max_weight < current:
#         max_count = i
#         max_weight = current
#     print(i, current)
# print(f"Мининмум. Арбуз № {min_count} , вес {min_weight}")
# print(f"Максимум. Арбуз № {max_count} , вес {max_weight}")

# ----------Задача---------
# Погода
# ----------Решение--------
from random import randint

day = int(input("Введите количество дней: "))
temp = 1
temp_inc_min = -3
temp_inc_max = 3
day_count = 0
day_max = 0
for i in range(day):
    temp_inc = randint(temp_inc_min, temp_inc_max)
    temp += temp_inc
    if temp > 0:
        day_count += 1
    else:
        day_count = 0
    if day_max < day_count:
        day_max = day_count
    print(f'{i}\t {temp}\t {temp_inc}\t {day_count}')
print('Оттепель длилась дней', day_max)
