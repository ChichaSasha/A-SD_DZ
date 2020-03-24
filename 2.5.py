n = int(input())
collect = input().split()
m = int(input())
to_check = sorted(input().split(), key=lambda i: int(i))
collect_max = int(collect[n - 1])

for i in range(m):
    if to_check[i] not in collect:
        print("No")
        if int(to_check[i]) > collect_max:
            break
    else:
        print("YES")
if i != m-1:
    for i in range(n - i - 1):
        print("NO")
