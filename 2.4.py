
def n_to_m(n):
    n_2 = ""
    # to base 2
    while n > 0:
        n_2 += str(n % 2)
        n = n // 2

    max_num = "0"

    for i in range(len(n_2)):
        n_2 = n_2[1:] + n_2[0]
        if n_2 > max_num:
            max_num = n_2
    # to base 10
    step = 1
    ans_num = 0
    for i in range(len(n_2) - 1, -1, -1):
        if max_num[i] == '1':
            ans_num += step
        step *= 2

    return ans_num

def other(n):
    n_2 = []
    # to base 2
    while n > 0:
        n_2.append(n % 2)
        n = n // 2

    max_num = n_2
    for i in range(len(n_2)):
        n_2 = n_2[1:] + [n_2[0]]
        if n_2 > max_num:
            print(n_2)
            max_num = n_2
    # to base 10
    step =
    ans_num = 0
    for i in range(len(n_2) - 1, -1, -1):
        if max_num[i] == 1:
            ans_num += step
        step *= 2

    return ans_num


n = int(input())
print(other(n))
print(n_to_m(n), '\n', other(n))
