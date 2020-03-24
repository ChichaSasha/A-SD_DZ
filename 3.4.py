from math import sin


def solve(f, a, b, c):
    m = (a + b) / 2.0
    while a != m and m != b:
        if f(m) < c:
            a = m
        else:
            b = m

        m = (a + b) / 2.0

    return a


a = 1.6
b = 3
print(solve(lambda x: sin(x) - x / 3, a, b, 0))
