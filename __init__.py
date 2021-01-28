import time
import random

from sort_utils import bubble_sort
from sort_utils import insertion_sort
from sort_utils import selection_sort
from sort_utils import merge_sort


def run_all():
    result = {}
    items_qty = 5000
    items = [random.randint(1, items_qty * 10) for _ in range(items_qty)]
    t1 = time.perf_counter()
    sorted_etalon = list(sorted(items))
    t2 = time.perf_counter()
    print(f'Etalon: {round(t2 - t1, 5)}')
    for name, functor in (
            ('Bubble', bubble_sort.sort),
            ('Insertion', insertion_sort.sort),
            ('Selection', selection_sort.sort),
            ('Merge', merge_sort.sort),
    ):
        t1 = time.perf_counter()
        sorted_items = functor(items[:])
        assert sorted_items == sorted_etalon
        t2 = time.perf_counter()
        result[name] = round(t2 - t1, 5)
        print(f'{name}: {result[name]}')


if __name__ == '__main__':
    run_all()
