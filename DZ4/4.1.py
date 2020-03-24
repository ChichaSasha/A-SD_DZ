lst = list(map(int, input().split()))

w = lst[0]
h = lst[1]
n = lst[2]

l = 0
r = w*n

while l < r:
    m = l + (r - l)//2
    k = (m//w)*(m//h)
    if k < n:
        l = m+1
    else:
        r = m

print(l)