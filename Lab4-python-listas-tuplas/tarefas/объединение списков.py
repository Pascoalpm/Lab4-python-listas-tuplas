#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой
    A = list(map(int, input().split()))

    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    print("Исходный список:", A)

    # 1. Произведение элементов с четными номерами
    product_even = 1
    for i in range(0, len(A), 2):
        product_even *= A[i]
    print("1. Произведение элементов с четными номерами:", product_even)

    # 2. Сумма между нулями
    if 0 in A:
        first_zero = A.index(0)
        last_zero = len(A) - 1 - A[::-1].index(0)

        if first_zero < last_zero:
            sum_between = sum(A[first_zero + 1:last_zero])
            print("2. Сумма между нулями:", sum_between)
        else:
            print("2. Между нулями нет элементов")
    else:
        print("2. В списке нет нулевых элементов")

    # 3. ПРЕОБРАЗОВАНИЕ - МЕТОД 2: объединение списков
    positive = []
    negative = []

    for item in A:
        if item >= 0:  # 0 считаем положительным
            positive.append(item)
        else:
            negative.append(item)

    # ОБЪЕДИНЕНИЕ списков операцией +
    A_transformed = positive + negative
    print("3. Преобразованный список (объединение):", A_transformed)