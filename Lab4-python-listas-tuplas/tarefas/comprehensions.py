#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Ввести список одной строкой
    A = list(map(int, input().split()))

    if len(A) != 10:
        print("Неверный размер списка")
        exit(1)

    # Найти индекс минимального элемента usando List Comprehension + функции агрегации
    min_value = min(A)  # функция min() из примеров
    i_min = A.index(min_value)  # метод index() из примеров
1
    # Переставить элементы
    A[i_min], A[-1] = A[-1], A[i_min]

    print("Преобразованный список:", A)