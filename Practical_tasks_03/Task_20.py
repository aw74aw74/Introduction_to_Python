# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква
# имеет определенную ценность. В случае с английским алфавитом
# очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков;
# J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются
# так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу,
# которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое
# содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12
def fill_dict(dict_def, string_def, nominal):
    for item in list(string_def):
        dict_def[item] = nominal
    return dict_def


dict_my = dict()
fill_dict(dict_my, "AEIOULNSTR", 1)
fill_dict(dict_my, "DG", 2)
fill_dict(dict_my, "BCMP", 3)
fill_dict(dict_my, "FHVWY", 4)
fill_dict(dict_my, "K", 5)
fill_dict(dict_my, "JX", 8)
fill_dict(dict_my, "QZ", 10)

fill_dict(dict_my, "АВЕИНОРСТ", 1)
fill_dict(dict_my, "ДКЛМПУ", 2)
fill_dict(dict_my, "БГЁЬЯ", 3)
fill_dict(dict_my, "ЙЫ", 4)
fill_dict(dict_my, "ЖЗХЦЧ", 5)
fill_dict(dict_my, "ШЭЮ", 8)
fill_dict(dict_my, "ФЩЪ", 10)

word_my = input("Введите слово: ")
summ = 0
for i in list(word_my):
    summ += dict_my[i.upper()]
print(summ)
