input_ = [int(i) for i in input().split()]
n, k = input_[0], input_[1]
lengths = []
for i in range(n):
    lengths.append(int(input()))

if not (1 <= n <= 10001 or 1 <= k <= 10001):
    raise ValueError


def func(chisla):
    l = 1
    r = sum(chisla) // k
    m = (l + r) // 2
    while l < r:
        s = 0
        for i in chisla:
            s += i // m
        if s >= k:
            l = m + 1
        else:
            r = m
        m = (l + r) // 2
    return l - 1


print(func(lengths))
