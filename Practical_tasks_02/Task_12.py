# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

number_s = int(input("Введите сумму двух чисел: "))
number_p = int(input("Введите их произведение: "))
for i in range(1000):
    for j in range(1000):
        if number_s == i + j and number_p == i * j:
            print(f"Задуманные числа {i} и {j}.")
