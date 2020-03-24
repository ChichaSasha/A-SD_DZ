def solve(f, a, b, c):
    m = (a + b) / 2.0
    while a != m and m != b:
        if f(m) < c:
            a = m
        else:
            b = m

        m = (a + b) / 2.0

    return a


a = 0
b = 10
print(solve(lambda x: x ** 3 + x + 1, a, b, 5.0000000000000001))
