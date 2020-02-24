from time import perf_counter


def padovan_recursion(n):
    if n <= 2:
        return 1
    else:
        return padovan_recurent(n - 1) + padovan_recurent(n - 3)


def padovan_recurent(n):
    if n <= 2:
        return 1

    a = 1
    b = 1
    c = 1

    for i in range(2, n + 1):
        a, b, c = b, c, c + a

    return c


start = perf_counter()
elem = padovan_recursion(10)
end = perf_counter()
timer = end - start
print("P10 = ", elem, "  Time for P10 (padovan_recursion) : ", timer)

start = perf_counter()
elem = padovan_recurent(10)
end = perf_counter()
timer = end - start
print("P10 = ", elem, "  Time for P10 (padovan_recurent) : ", timer)

start = perf_counter()
elem = padovan_recursion(20)
end = perf_counter()
timer = end - start
print("P10 = ", elem, "  Time for P20 (padovan_recursion) : ", timer)

start = perf_counter()
elem = padovan_recurent(20)
end = perf_counter()
timer = end - start
print("P10 = ", elem, "  Time for P20 (padovan_recurent) : ", timer)

start = perf_counter()
elem = padovan_recursion(50)
end = perf_counter()
timer = end - start
print("P10 = ", elem, "  Time for P50 (padovan_recursion) : ", timer)

start = perf_counter()
elem = padovan_recurent(50)
end = perf_counter()
timer = end - start
print("P10 = ", elem, "  Time for P50 (padovan_recurent) : ", timer)