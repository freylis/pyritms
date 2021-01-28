"""
Сортировка выбором

Бежим по массиву из N элементов N раз, запоминая позицию I
    Бежим по массиву от позиции I до конца, запоминая минимальный встреченный элемент и его позицию K
    Меняем местами элементы в позиции I и K

n^2
"""
from sort_utils import base


def sort(items):
    for index in range(len(items)):
        min_element = None
        subindex = 0
        index_for_replace = None
        for subindex, tmp_val in enumerate(items[index:]):
            if min_element is None:
                min_element = tmp_val
                index_for_replace = subindex
                continue
            if tmp_val < min_element:
                min_element = tmp_val
                index_for_replace = subindex
                continue
        if index_for_replace and index != subindex:
            items[index], items[index_for_replace + index] = items[index_for_replace + index], items[index]
    return items


if __name__ == '__main__':
    base.sorting_checker(sort)
