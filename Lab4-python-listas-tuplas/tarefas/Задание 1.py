#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Ввести список одной строкой
    A = list(map(int, input().split()))

    # Проверить количество элементов списка
    if len(A) != 10:
        print("Неверный размер списка")
        exit(1)

    # Найти наименьший элемент и его индекс
    a_min = A[0]
    i_min = 0

    for i, item in enumerate(A):
        if item < a_min:
            i_min, a_min = i, item

    # Переставить наименьший элемент с последним
    A[i_min], A[-1] = A[-1], A[i_min]

    print("Преобразованный список:", A)