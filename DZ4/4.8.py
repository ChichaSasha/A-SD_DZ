class t_list():

    def __init__(self, lst = []):
        lst.sort()
        self.lst = [[el, el] for el in lst]

    def __len__ (self):
        return len(self.lst)

    def create(self, lst):
        lst.sort()
        self.lst = [[el, el] for el in lst]

    def add(self, val, t):
        left = 0
        right = len(self.lst)
        while left < right:
            m = left + (right - left) // 2
            if self.lst[m][0] <= val:
                left = m + 1
            else:
                right = m

        self.lst.insert(left, [val, t])

    def delete(self, ind):
        el = self.lst.pop(ind)
        return el[0], el[1]

    def get(self, ind):
        return self.lst[ind]

    def clear(self):
        self.lst = []

    def binary_search(self, x, array):
        left = 0
        right = len(self.lst) - 1
        while left < right:
            m = left + (right - left) // 2
            if array[m][0] < x:
                left = m + 1
            else:
                right = m

        return left

    def __str__(self):
        return '  '.join(str(el) for el in self.lst)


N = int(input())
Na = int(input())
A = list(map(int, input().split()))
Nb = int(input())
B = list(map(int, input().split()))
'''N = 6
Na = 3
A = [1,3,2]
Nb = 2
B = [2,3]'''

A_obj = t_list(A)
B_obj = t_list()
resa = []
ll = len(B)

for i in range(N):
    a, t = A_obj.delete(0)
    resa.append(a)
    A_obj.add(a + t, t)

l = resa[-1]
r = 10**3

while l < r:
    print('|')
    w = 0
    m = l + (r - l)//2
    B_obj.create(B)
    for i in range(N-1,-1,-1):
        y = m - resa[i]
        if y < B_obj.lst[0][0]:
            w += 1
            break
        else:
            ind = B_obj.binary_search(y, B_obj.lst)
            x = B_obj.lst[ind][0]

            if x > y:
                ind -= 1
            a, t = B_obj.get(ind)
            B_obj.delete(ind)
            B_obj.add(a+t,t)
            print(B_obj)
    if w == 0:
        r = m
    else:
        l = m + 1
    B_obj.clear()

print(l)