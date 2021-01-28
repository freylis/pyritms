"""
Сортировка слиянием.
Рекурсивно делим список на пополам, до тех пор, пока в левом и правом списках не больше одного элемента
Объединяем оба списка в один, выбирая минимальный элемент в цикле из левой или правой половины.

log(n)
"""
from sort_utils import base


def sort(items, left=0, right=None):
    """
    Рекурсивно сливаем две половины, отсортированные в нужном порядке
    """
    if right is None:
        right = len(items)
    center = left + int((right - left) / 2)
    if (center - left) < 2 and (right - center) < 2:
        items = _merge(items, left=left, center=center, right=right)
        return items

    items = sort(items, left=left, right=center)
    items = sort(items, left=center, right=right)
    items = _merge(items, left=left, center=center, right=right)
    return items


def _merge(items, left, center, right):
    """
    Слияние двух подмассивов items[left:center] и items[center:right]
    """
    left_items, right_items = items[left:center], items[center:right]

    for index in range(right - left):
        if not left_items and not right_items:
            break
        if (
                not left_items
                or (
                    left_items
                    and right_items
                    and left_items[0] > right_items[0]
                )
            ):
            value = right_items.pop(0)
        else:
            value = left_items.pop(0)

        items[left + index] = value

    return items


if __name__ == '__main__':
    base.sorting_checker(sort)
