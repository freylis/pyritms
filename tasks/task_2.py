import random

from search_utils import binary_search
from sort_utils import merge_sort


def task_2_3_7(items, expect_sum):
    """
    Определить, имеются ли в <items> два значения, сумма которых == <expect_sum>
    """
    items = merge_sort.sort(items)
    # если число четное -- искомый результат может быть суммой двух одинаковых чисел
    if not expect_sum % 2:
        half_expect_sum = expect_sum / 2
        first_index = binary_search.search(items, half_expect_sum)
        items_v1 = items.pop(first_index)
        second_index = binary_search.search(items, items_v1)
        if first_index != -1 and second_index != -1:
            return True

    for val in range(1, expect_sum):
        # если элемента нет в списке - сразу нет
        if binary_search.search(items, val) == -1:
            continue
        # первая часть есть. посмотрим на наличие второй части
        second_val = expect_sum - val
        if binary_search.search(items, second_val) != -1:
            return True

    return False


if __name__ == '__main__':
    assert task_2_3_7([], 1) is False
    assert task_2_3_7([1, 1], 2) is True
    assert task_2_3_7([5, 7, 9, 10], 19) is True
    assert task_2_3_7([5, 7, 9, 10], 20) is False
    assert task_2_3_7([10, 20, 30, 40, 50, 60], 100) is True
    assert task_2_3_7([10, 20, 30, 40, 50, 60], 11) is False
