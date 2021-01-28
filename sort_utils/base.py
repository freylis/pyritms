import random


def sorting_checker(functor):
    assert functor([]) == []
    assert functor([1]) == [1]
    assert functor([2, 1]) == [1, 2]
    assert functor([2, 1, 3]) == [1, 2, 3]

    values = [random.randint(-100, 100) for _ in range(100)]
    assert sorted(values) == functor(values)
