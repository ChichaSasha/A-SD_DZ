"""
Реалізуйте підпрограму сортування масиву.
"""


def arraySortedOrNot(arr, n):
    if (n == 0 or n == 1):
        return True

    for i in range(1, n):

        if (arr[i - 1] > arr[i]):
            return False

    return True


# бульбашкой
def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        if arraySortedOrNot():
            break

    return array


# вибором
# def sort(array):
#     for i in range(len(array) - 1, 0, -1):
#         maxpos = 0
#         for j in range(1, i + 1):
#             if array[maxpos] < array[j]:
#                 maxpos = j
#         array[i], array[maxpos] = array[maxpos], array[i]

# вставкою
def sort(array):
    for index in range(1, len(array)):
        currentValue = array[index]
        position = index
        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        # Вставка поточного елемента у знайдену позицію
        array[position] = currentValue
