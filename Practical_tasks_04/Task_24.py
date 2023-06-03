# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по
# окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом
# кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система
# автоматического сбора черники. Эта система состоит из управляющего модуля
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с
# двух соседних с ним. Напишите программу для нахождения максимального числа
# ягод, которое может собрать за один заход собирающий модуль, находясь перед
# некоторым кустом заданной во входном файле грядки.
import random

count_bush = int(input("Введите количество кустов на грядке: "))
if count_bush < 3:
    print("Собирать нужно куста 1")
elif count_bush == 3:
    print("Собирать нужно с куста 2")
else:
    bush_blueberries = list()
    for i in range(count_bush):
        bush_blueberries.append(random.randint(1, 10))
        print("Куст - {}, ягод - {}".format(i + 1, bush_blueberries[i]))
    bush_blueberries.append(bush_blueberries[0])
    bush_blueberries.append(bush_blueberries[1])
    max_blueberries = 0
    start_bush = 0
    for i in range(1, count_bush + 1):
        current_blueberries = (
            bush_blueberries[i - 1] + bush_blueberries[i] + bush_blueberries[i + 1]
        )
        if max_blueberries < current_blueberries:
            max_blueberries = current_blueberries
            start_bush = i
    if start_bush > count_bush - 1:
        start_bush -= count_bush
    print("Собирать нужно с куста {}".format(start_bush + 1))
