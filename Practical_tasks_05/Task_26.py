# Задача 26:  Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def stepen_rec(a, b):
    if b < 1:
        return 1
    else:
        result = 1
        for i in range(b):
            result = a * stepen_rec(a, b - 1)
        return result

number_a = int(input("Введите число A: "))
number_b = int(input("Введите число B: "))
print(stepen_rec(number_a, number_b))
