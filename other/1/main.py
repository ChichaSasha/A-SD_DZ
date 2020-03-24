import time

import numpy
import user

N = 1000  # Кількість елементів масиву


def checkResult(array):
    """ Перевіряє впорядкованість масиву даних за зростанням
    :param array: масив
    """
    errors = 0
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            errors += 1

    print("Errors:       ", errors)


def testSort():

    s = numpy.random.randint(0, 10000, N)
    t = time.process_time()
    result = user.sort(s)
    dt = time.process_time() - t
    print('Sorting time: ', dt)
    checkResult(result)


if __name__ == "__main__":
    testSort()