"""
Сортировка вставкой:

Бежим по списку из N-элементов N-раз, запоминая текущую позицию I
    Если I > I + 1 - меняем местами
    В следующий раз сравниваем I - 1 с I

Берем элемент, справниваем его с следующим. Если следующий меньше -- меняем их местами

k*n*log(n)
"""
from sort_utils import base


def sort(items):
    for index in range(len(items)):
        if not index:
            continue

        subindex = index - 1
        while subindex > -1 and items[subindex] > items[subindex + 1]:
            items[subindex], items[subindex + 1] = items[subindex + 1], items[subindex]
            subindex -= 1

    return items


if __name__ == '__main__':
    base.sorting_checker(sort)
