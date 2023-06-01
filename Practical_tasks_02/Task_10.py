# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

money = int(input("Введите количество монет: "))
money_reshka = 0
money_orel = 0
print("Монеты: ", end="")
for i in range(money):
    money_current = randint(0, 1)
    print(money_current, end="")
    if money_current == 0:
        money_reshka += 1
    else:
        money_orel += 1
print()
print(f"Монет решкой вверх {money_reshka} шт.")
print(f"Монет орлом вверх {money_orel} шт.")
if money_reshka > money_orel:
    print(f"Надо перевернуть все монеты, расположенные орлом вверх.")
elif money_reshka < money_orel:
    print(f"Надо перевернуть все монеты, расположенные решкой вверх.")
else:
    print(f"Можно перевернуть любой набор монет.")
