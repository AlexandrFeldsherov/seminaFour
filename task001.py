# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import function


def search_prime_factors(value: int) -> list:
    i = 2
    lst = []
    while i <= value:
        if value % i == 0:
            lst.append(i)
            value //= i
            i += 1
        else:
            i += 1
    return lst


num = function.input_int_numbers()
lst = search_prime_factors(num)

print(f"Простые множители числа {num} приведены в списке: {lst}")
