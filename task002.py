# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

import function

def uniq_number(arr:list)->list:
    """
    Убирает повторы в списке
    """
    r=[]
    for a in arr:
        if not a in r:
            r.append(a)
    return r

entered_list = list(map(int, input("Введите числа через пробел:\n").split()))
lst_new=uniq_number(entered_list)
print(f"{entered_list} -> {lst_new}")
