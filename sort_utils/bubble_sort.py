"""
Пузырёк родной, три семерочки.
Сложность n^2
"""
from sort_utils import base


def sort(items):
    """
    Отсортировать методом пузырька
    """
    last = None
    for _ in range(len(items)):
        moved = False
        for index, x in enumerate(items):
            if index == 0:
                last = x
                continue

            # если текущий элемент меньше предыдущего - поменять их местами
            if x < last:
                items[index - 1], items[index] = items[index], items[index - 1]
                moved = True
            last = x
        if not moved:
            break
    return items


if __name__ == '__main__':
    base.sorting_checker(sort)
