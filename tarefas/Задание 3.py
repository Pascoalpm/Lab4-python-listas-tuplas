#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Ввести оценки
    A = tuple(map(int, input().split()))

    if len(A) != 24:
        print("Неверное количество оценок")
        exit(1)

    # Подсчитать пятерки - метод count() из примеров с кортежами
    count_5 = A.count(5)

    # Создать упорядоченный список (потом преобразуем в кортеж)
    sorted_list = []

    # Сначала добавить все пятерки
    for i in range(count_5):
        sorted_list.append(5)

    # Затем добавить остальные оценки
    for grade in A:
        if grade != 5:
            sorted_list.append(grade)

    # Преобразовать в кортеж (функция tuple() из примеров)
    sorted_grades = tuple(sorted_list)

    print("Количество пятерок:", count_5)
    print("Упорядоченные оценки:", sorted_grades)