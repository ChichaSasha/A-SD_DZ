def binary_search(arr, l, r, x):
    if (r < l):
        return -1

    m = l + (r - l) // 2

    if arr[m] == x:
        return m

    if arr[m] > x:
        return binary_search(arr, l, m - 1, x)

    return binary_search(arr, m + 1, r, x)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr[binary_search(arr, 0, 10, 5)])