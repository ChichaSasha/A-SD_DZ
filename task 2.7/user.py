"""
Знайдіть кількість входжень заданого числа x до впорядкованого за неспаданням масиву цілих чисел array
"""
import numpy

def counter(array, x):
    """ кількість входжень заданого числа.
    :param array: Масив цілих чисел впорядкований за неспаданням
    :param x:     Шуканий елемент
    :return:      Кількість входжень
    """
    # TODO: Реалізуйте алгоритм тут.
    def bsearch_rightmost(array, x):
        l = 0
        r = len(array)
        while l < r:
            m = l + (r - l) // 2
            if array[m] <= x:
                l = m + 1
            else:
                r = m
        return l - 1

    def bsearch_leftmost(array, x):
        l = 0
        r = len(array) - 1
        while l < r:
            m = l + (r - l) // 2
            if array[m] < x:
                l = m + 1
            else:
                r = m
        return l
    l = bsearch_leftmost(array, x)
    r = bsearch_rightmost(array, x)
    if array[l] != x or array[r] != x:
        return 0
    return r - l + 1