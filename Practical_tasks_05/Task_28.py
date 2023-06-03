# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4


def summ_rec(a, b, result):
    # result = 0
    if a < 1 and b < 1:
        return result
    if a > 0:
        result += 1
    if b > 0:
        result += 1
    return summ_rec(a - 1, b - 1, result)


number_a = int(input("Введите число A: "))
number_b = int(input("Введите число B: "))
print(summ_rec(number_a, number_b, 0))
