"""
Бинарный поиск
На входе сортированный массив числе и искомое значение
На выходе индекс искомого значения, если он есть. Если нет - -1
"""
import random


def search(items, value, left=0):
    """
    Args:
        items (list[int|float]):
        value (int|float):
        tmp_position (int|None):
        is_left (bool):

    Returns:
        int|None
    """
    if not items:
        return -1

    length = len(items)
    center = int(length / 2)
    center_value = items[center]

    # если значение нужное - можно спросить справа
    if center_value == value:
        index = search(
            items=items[:center],
            value=value,
            left=left,
        )
        # если ничего не найдено в левой части, значит искомый индекс -- индекс текущего элемента
        if index == -1:
            return left + center
        return index

    # если центральный элемент меньше искомого, истина находится в левой сторое
    if center_value > value:
        return search(
            items=items[:center],
            value=value,
            left=left,
        )
    else:
        return search(
            items=items[center + 1:],
            value=value,
            left=left + center + 1,
        )


if __name__ == '__main__':
    for items, value, index in (
       ([], 1, -1),
       ([1, 2, 5], 2, 1),
       ([1, 2, 4, 5], 2, 1),
       ([1, 2, 5], 1, 0),
       ([1, 2, 4, 5], 1, 0),
       ([11, 12, 17, 27, 400], 400, 4),
       ([11, 12, 17, 27, 399, 400], 400, 5),
       ([11, 12, 17, 27, 400], 27, 3),
       ([11, 12, 17, 27, 399, 400], 27, 3),
       ([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 7], 4, 7),
       ([-10, -6, -3, -2, -2, 2, 2, 4, 5, 6, 9], -6, 1),
        ([-7, -7, -5, 0, 1, 1, 3, 3, 4, 6, 7], 6, 9),
    ):
        found_index = search(items, value)
        assert found_index == index, f'Search {value} in {items}. Found in p{found_index}, expect p{index}'

    for expect_value in (-6, 6):
        for index in range(10):
            rnd_list = list(sorted([random.randint(-10, 10) for _ in range(10)] + [expect_value]))
            found_index = search(rnd_list, expect_value)
            assert found_index == rnd_list.index(expect_value), f'{index} / Search {expect_value} in {rnd_list}. ' \
                                                                f'Found {found_index}, expect ' \
                                                                f'{rnd_list.index(expect_value)}'
