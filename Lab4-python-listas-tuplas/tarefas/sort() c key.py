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
    for i in range(len(A)):
        if i % 2 == 0:
            product_even *= A[i]
    print("1. Произведение элементов с четными номерами:", product_even)

    # 2. Сумма между нулями
    if 0 in A:
        first_zero = A.index(0)
        last_zero = first_zero
        for i in range(len(A)):
            if A[i] == 0:
                last_zero = i

        if last_zero > first_zero:
            sum_between = 0
            for i in range(first_zero + 1, last_zero):
                sum_between += A[i]
            print("2. Сумма между нулями:", sum_between)
        else:
            print("2. Между нулями нет элементов")
    else:
        print("2. В списке нет нулевых элементов")


    # 3. ПРЕОБРАЗОВАНИЕ - МЕТОД 1: sort() с key
    def sort_key(x):
        return 1 if x < 0 else 0  # отрицательные -> 1, остальные -> 0


    A.sort(key=sort_key)
    print("3. Преобразованный список (sort+key):", A)