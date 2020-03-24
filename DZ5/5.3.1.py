from bisect import bisect_left
from collections import defaultdict
M = 9999991# 100007
N = 51

class MaClass:
    def __init__(self):
        self.authors = [None for i in range(M)]
        self.books = [None for i in range(M)]

    def H(self,s):
        h = 0
        for c in s:
            h = h * N + ord(c)
        return h % M

    def func(self,s):
        res = ""
        for i in range(len(s)):
            res += s[i] + ', '
        res = res[:len(res) - 2:]
        return res

    def addBook(self, author, title):
        cur = self.H(author)
        while self.authors[cur] is not None:
            if self.authors[cur] == author:
                num = bisect_left(self.books[cur], title)
                if not (num < len(self.books[cur]) and self.books[cur][num] == title):
                    self.books[cur].insert(num, title)
                return
            cur = (cur + N) % M
        self.authors[cur] = author
        self.books[cur] = [title]

    def find(self, author, title):
        cur = self.H(author)
        while self.authors[cur] is not None:
            if self.authors[cur] == author:
                num = bisect_left(self.books[cur], title)
                return True if num < len(self.books[cur]) and title == self.books[cur][num] else False
            cur = (cur + N) % M
        return False

    def findByAuthor(self, author):
        cur = self.H(author)
        while self.authors[cur] is not None:
            if self.authors[cur] == author:
                return self.books[cur]
            cur = (cur + N) % M
        return []

    def findByAuthor_(self, author):
        cur = self.H(author)
        while self.authors[cur] is not None:
            if self.authors[cur] == author:
                return self.func(self.books[cur])
            cur = (cur + N) % M
        return []
n = 3
l_to_e = defaultdict(list)
obj1 = MaClass()

for i in range(n):
    e_word, l_words = input().split(' - ')
    l_trans = l_words.split(', ')
    for l in l_trans:
        obj1.addBook(l, e_word)
        l_to_e[l].append(e_word)

print(len(l_to_e))
for wrd in sorted(l_to_e):
    print(wrd, ' - ', obj1.findByAuthor_(wrd))




